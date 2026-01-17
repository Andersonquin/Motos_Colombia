
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Importa esto
from database_manager import DatabaseManager

app = FastAPI()
db = DatabaseManager()

# ESTO ES LO NUEVO: Permite que tu HTML lea la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"mensaje": "API Activa"}

@app.get("/motos")
def listar_motos():
    datos = db.obtener_todas_las_motos()
    return {"motos": datos}

@app.get("/motos/{id_moto}")
def consultar_moto_por_id(id_moto: int):
    # Aquí buscamos en la lista por su posición (o podrías hacer un SELECT en la DB)
    motos = db.obtener_todas_las_motos()
    if id_moto < len(motos):
        return {"resultado": motos[id_moto]}
    return {"error": "Moto no encontrada"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Importa esto
from database_manager import DatabaseManager


