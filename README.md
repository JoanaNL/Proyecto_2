# PROYECTO 2 #

Del marketing bancario en campañas personalizadas a la integración en el ecosistema Saleforce CRM

# Introducción: #

Mi nombre es Joana, una analista y científica de datos que empezó estudiando un grado superior en administración y finanzas, después pasé a estudiar y hacer lo que representa mi auténtica vocación, dedicarme a un grado superior en ilustración y animación 2D y 3D, y más tarde, después de haber experimentado muchas vivencias personales y profesionales de todo tipo, decidí dar un vuelco a mi vida profesional y apostar por introducirme progresivamente en el mundo del Big Data, Análisis de Datos, Salesforce CRM, SQL, etc… y esto me llevó a iniciar un Máster de Data Science & IA con Evolve Academy de forma casi inesperada, y la verdad es que me encanta la idea de poder combinar el análisis de datos con un CRM potente como es Salesforce, me gustaría en un futuro poder trabajar como analista, científica de datos o en el mundo de los datos en combinación con Salesforce CRM en alguna empresa tecnológica que lo utilice y sea puntera.

Por otro lado, lo que hizo también que finalmente me decidiera a estudiar y formarme en este sector fueron mis últimas experiencias laborales.

Continúo en constante aprendizaje aplicando la mentalidad de crecimiento, persistencia, ganas y motivación con las herramientas de datos que he ido aprendiendo a usar todos estos meses.


# Herramientas principales utilizadas en el proyecto: #

Canva, ChatGPT, ClickUp, Docker, FastApi Swagger, Git Bash, GitHub
Jupyter, Kaggle, Postman, 
Python (librerias: pandas, numpy, scikit-learn, sklearn, uvicorn, matplolib, joblib, fastapi, pydantic, os, warnings, etc…)
Render, Salesforce Developer Edition, Streamlit, Terminal Bash
VSC (Visual Studio Code)

# Técnicas utilizadas para ML: #

En este proyecto de MVP, he entrenado un modelo de clasificación y regresión logística para predecir qué probabilidad en base a unas determinadas características de clientes del BBDD elegida, posteriormente una vez entrenado y desplegado el modelo entrenado en Docker y Render, después lo he aplicado en FastAPI y he podido ejecutar una prueba del cuál me ha dado unos resultados que esperaba tener.

Descripción proyecto/dataset:

# Mejora del marketing para personalizar campañas a segmentos de clientes y conseguir mejorar la contratación depósitos en base a las características de los clientes a través de predicciones automatizadas por IA.

El dataset utilizado para este proyecto lo encontré e importé desde Kaggle, trata sobre un único producto a analizar, es decir, contratar un depósito, y predecir si en base a las características del cliente comprará el producto o no. 

Esto es muy útil en un sistema de gestión de clientes para elegir a qué clientes ofrecerles un producto determinado porque haya probabilidad de compra, y linka directamente con Salesforce como sistema de gestión comercial de clientes.

Este dataset está basado en campañas de marketing personalizadas para un segmentos de clientes potenciales que estén interesados y/o estén buscando la forma de invertir su capital/ahorros sin riesgos, con garantías y rentabilidad fija todos los meses y años. 

La variables y columnas que aparecen en el dataset son los siguientes:

* Demografía del cliente: *age*, *job*, *marital*, *education*
* Información financiera: *balance*, *housing*, *loan*, *default*
* Interacciones de campaña: *duration*, *campaign*, *pdays*, *previous*, *poutcome*
* Objetivo (*response*) y su versión binaria (*response_binary*)


# Objetivos y/o cuestiones a resolver:

Analizar características de los clientes (como datos demográficos e historial de transacciones).
Predecir la probabilidad de que un cliente acepte un depósito a plazo fijo dependiendo del mercado objetivo.
Identificar perfiles para personalizar futuras campañas dirigido solo al cliente potencial.


# Descripción del dataset:

Contiene 41,188 observaciones, cada una representando un cliente contactado por teléfono.
Tiene 16 variables de entrada (edad, ocupación, estado civil, etc.).
Una única variable de salida binaria: y (respuesta: “yes” o “no”).


URL's utilizadas en el proyecto:

* URL FastAPI / Docker: http://127.0.0.1:8000/docs#/default/predecir_endpoint_predecir_post

* URL NGrok: https://be88-83-42-202-6.ngrok-free.app -> http://localhost:8000

* OAuth 2.0: add-authtoken 2ybNhnvUY4C7gn1oP7GdkDlpJyf_7bUnCt21iMmJTmWc4y86T

* URL Render: https://api-modelo-kbw3.onrender.com



