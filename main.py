from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Mi API", version="1.0.0")

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>FastAPI - Inicio</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    text-align: center;
                }
                h1 { color: #009688; }
                .endpoint {
                    background: #f5f5f5;
                    padding: 15px;
                    margin: 10px 0;
                    border-radius: 5px;
                    text-align: left;
                }
                code {
                    background: #333;
                    color: #fff;
                    padding: 2px 8px;
                    border-radius: 3px;
                }
            </style>
        </head>
        <body>
            <h1>🚀 FastAPI - Aplicación Base</h1>
            <p>Tu API está funcionando correctamente</p>
            
            <div class="endpoint">
                <h3>Endpoints disponibles:</h3>
                <p><code>GET /</code> - Esta página</p>
                <p><code>GET /api/hello</code> - Saludo JSON</p>
                <p><code>GET /api/items/{item_id}</code> - Obtener item por ID</p>
                <p><code>GET /docs</code> - Documentación interactiva (Swagger)</p>
                <p><code>GET /redoc</code> - Documentación alternativa</p>
            </div>
        </body>
    </html>
    """

@app.get("/api/hello")
async def hello():
    return {"mensaje": "¡Hola desde FastAPI!"}

@app.get("/api/items/{item_id}")
async def get_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}

@app.post("/api/items")
async def create_item(name: str, price: float):
    return {
        "mensaje": "Item creado",
        "item": {"name": name, "price": price}
    }
