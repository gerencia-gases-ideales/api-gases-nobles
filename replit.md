# Proyecto FastAPI

## Descripción
Aplicación base con FastAPI, un framework moderno y rápido para crear APIs con Python.

## Estructura del Proyecto
```
.
├── main.py           # Archivo principal de la aplicación
├── requirements.txt  # Dependencias de Python
└── .gitignore       # Archivos ignorados por git
```

## Tecnologías
- **FastAPI**: Framework web moderno para crear APIs
- **Uvicorn**: Servidor ASGI de alto rendimiento

## Endpoints Disponibles
- `GET /` - Página de inicio HTML
- `GET /api/hello` - Endpoint de ejemplo que retorna JSON
- `GET /api/items/{item_id}` - Obtener item por ID
- `POST /api/items` - Crear un nuevo item
- `GET /docs` - Documentación interactiva automática (Swagger UI)
- `GET /redoc` - Documentación alternativa (ReDoc)

## Documentación
FastAPI genera documentación automática. Visita:
- `/docs` para Swagger UI (interactivo)
- `/redoc` para ReDoc

## Fecha de Creación
Diciembre 5, 2025
