# 🧠 Plantilla Base: Regresión Logística con Scikit-learn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


# 1. Cargar dataset
df = pd.read_csv("tu_archivo.csv")  # Cambia el nombre del archivo

# 2. Definir variables predictoras y objetivo
X = df[['columna1', 'columna2', 'columna3']]  # Reemplaza con tus columnas
y = df['target_binaria']  # Reemplaza con tu variable objetivo (0/1)

# 3. Separar variables numéricas y categóricas
num_features = ['columna1']            # Reemplaza según tu dataset
cat_features = ['columna2', 'columna3']  # Reemplaza según tu dataset

# 4. Preprocesamiento
preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', num_features),
        ('cat', OneHotEncoder(drop='first'), cat_features)
    ]
)

# 5. Construir pipeline con regresión logística
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000))
])

# 6. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Entrenar modelo
pipeline.fit(X_train, y_train)

# 8. Evaluar resultados
y_pred = pipeline.predict(X_test)
print("📊 Matriz de Confusión:")
print(confusion_matrix(y_test, y_pred))
print("\n📋 Reporte de Clasificación:")
print(classification_report(y_test, y_pred))

# O también:

y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))


# 9. Obtener probabilidades
y_prob = pipeline.predict_proba(X_test)[:, 1]
