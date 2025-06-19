import yaml

# Diccionari amb dades a desar
esquema = {
    "openapi": "3.0.0",
    "info": {
        "title": "API Modelo de Predicción",
        "version": "1.0"
    },
    "paths": {
        "/predecir": {
            "post": {
                "summary": "Predecir cliente",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Cliente"
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Probabilidad retornada",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Respuesta"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

# Crear el fitxer YAML
with open("openapi.yaml", "w", encoding="utf-8") as f:
    yaml.dump(esquema, f, sort_keys=False)
