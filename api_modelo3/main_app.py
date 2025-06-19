from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Cargar el modelo
modelo = joblib.load("C:\\Users\\Haine\\OneDrive\\Escritorio\\Proyecto_2\\api_modelo2\\modelo_regresion.pkl")
columnas_esperadas = modelo.feature_names_in_

# Definir la app
app = FastAPI()

# Esquema de entrada
class EntradaModelo(BaseModel):
    age: int
    balance: float
    campaign: int
    job: str
    marital: str
    education: str
    default: str
    housing: str

@app.post("/predecir_duration")
def predecir(entrada: EntradaModelo):
    # Convertir a DataFrame
    df = pd.DataFrame([entrada.dict()])

    # Codificar variables categóricas
    df_encoded = pd.get_dummies(df)

    # Alinear con las columnas del modelo
    df_alineado = df_encoded.reindex(columns=columnas_esperadas, fill_value=0)

    # Predecir duración
    pred = modelo.predict(df_alineado)[0]

    return {"prediccion_duration": float(pred)}
