# ISHI Anemia Detection API

This is a cloud-based Python FastAPI app that wraps the MED-B/AnemiaDetector model.
It receives an image via `/predict` and returns `{ "anemic": true/false }`.

## Structure
- `anemia_detector/`: ML model
- `app/main.py`: FastAPI app
- `requirements.txt`: dependencies

## To run:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
