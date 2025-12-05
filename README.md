# FastAPI - Aplicación Base

API REST construida con FastAPI.

## Instalación Local

```bash
pip install -r requirements.txt
```

## Ejecutar en desarrollo

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## Endpoints

- `GET /` - Página de inicio
- `GET /api/hello` - Saludo JSON
- `GET /api/items/{item_id}` - Obtener item por ID
- `POST /api/items` - Crear item
- `GET /docs` - Documentación Swagger
- `GET /redoc` - Documentación ReDoc

## Deploy en Render

1. Sube este repositorio a GitHub
2. Conecta tu cuenta de Render con GitHub
3. Crea un nuevo "Web Service"
4. Selecciona tu repositorio
5. Render detectará automáticamente la configuración
