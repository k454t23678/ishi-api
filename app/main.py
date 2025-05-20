# app/main.py

from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from anemia_detector.model_utils import load_model, predict_anemia

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

model = load_model()

@app.post("/predict")
async def predict(
    hemoglobin: float = Form(...),
    mch: float = Form(...),
    mchc: float = Form(...),
    mcv: float = Form(...),
    gender: int = Form(...)
):
    try:
        features = {
            "Hemoglobin": hemoglobin,
            "MCH": mch,
            "MCHC": mchc,
            "MCV": mcv,
            "GENDER": gender
        }

        result = predict_anemia(model, features)
        return {"anemic": result}
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

