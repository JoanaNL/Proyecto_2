
FROM python:3.10-slim

WORKDIR /app

COPY modelo_entrenado_v170.pkl .
COPY api_modelo.py .

RUN pip install fastapi uvicorn scikit-learn joblib pydantic

EXPOSE 8000

CMD ["uvicorn", "api_modelo:app", "--host", "0.0.0.0", "--port", "8000"]
