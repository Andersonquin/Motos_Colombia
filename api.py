from fastapi import FastAPI, HTTPException # Agregamos HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel # <--- NUEVO: Para validar los datos
from database_manager import DatabaseManager

app = FastAPI()
db = DatabaseManager()

# Configuración de CORS (Ya lo tenías, perfecto para el index.html)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# <--- NUEVO: Definimos qué datos necesita una moto
class Moto(BaseModel):
    marca: str
    referencia: str
    cilindraje: int  
    precio: float
    color: str

@app.get("/")
def home():
    return {"mensaje": "API Activa"}

@app.get("/motos")
def listar_motos():
    datos = db.obtener_todas_las_motos()
    return {"motos": datos}

# <--- NUEVO: Ruta para GUARDAR motos desde el frontend
@app.post("/motos")
def crear_moto(moto: Moto):
    try:
        db.guardar_moto(moto)
        return {"mensaje": "Moto guardada con éxito", "moto": moto}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar: {e}")

@app.get("/motos/{id_moto}")
def consultar_moto_por_id(id_moto: int):
    # Nota profesional: En lugar de len(), lo ideal sería un SELECT WHERE id=...
    # Pero por ahora, para tu lógica actual:
    motos = db.obtener_todas_las_motos()
    # Buscamos el ID real en la base de datos
    moto_encontrada = next((m for m in motos if m["id"] == id_moto), None)
    
    if moto_encontrada:
        return {"resultado": moto_encontrada}
    raise HTTPException(status_code=404, detail="Moto no encontrada")