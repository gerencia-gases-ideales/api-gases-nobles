from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="GASES NOBLES", version="1.0.0")

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las solicitudes de cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los headers
)

# Constante de gases
R = 0.082

# Página de inicio
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>FastAPI - Inicio</title>
        </head>
        <body>
            <h1>API de Ley de Gases Ideales</h1>
            <p>Tu API está funcionando correctamente.</p>
            <p>Visita <a href="/docs">/docs</a> para usar la documentación interactiva.</p>
        </body>
    </html>
    """


# Modelo para la API
class GasRequest(BaseModel):
    P: Optional[float] = None
    V: Optional[float] = None
    n: Optional[float] = None
    T: Optional[float] = None


# Endpoint principal
@app.post("/api/calcular-gas")
async def calcular_gas(req: GasRequest):
    valores = [req.P, req.V, req.n, req.T]
    missing = sum(1 for v in valores if v is None)

    if missing != 1:
        return {"error": "Debes dejar exactamente UNA variable vacía para calcularla."}

    P, V, n, T = req.P, req.V, req.n, req.T

    if P is None:
        P = (n * R * T) / V
    elif V is None:
        V = (n * R * T) / P
    elif T is None:
        T = (P * V) / (n * R)

    return {
        "P": P, "V": V, "n": n, "T": T, "R": R,
        "mensaje": "Cálculo realizado usando PV = nRT"
    }

