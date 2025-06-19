# Imagen base
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY app.py modelo_regresion.pkl ./
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 8000

# Comando para arrancar el servidor
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

