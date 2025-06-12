
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Carregar el model entrenat
model_path = os.path.join(os.path.dirname(__file__), "modelo_entrenado_v170.pkl")
model = joblib.load(model_path)

# Crear instància de FastAPI
app = FastAPI()

# Definir el model de dades d'entrada
class Cliente(BaseModel):
    age: int
    balance: float
    campaign: int

# Definir l'endpoint
@app.post("/predecir")
def predecir(cliente: Cliente):
    # Convertir les dades a array per a predicció
    datos = np.array([[cliente.age, cliente.balance, cliente.campaign]])
    prob = model.predict_proba(datos)[0][1]
    return {"probabilidad_si": prob}

