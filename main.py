# Archivo: main.py
from moto import Moto
from database_manager import DatabaseManager

# 1. Preparar la base de datos
db = DatabaseManager()
db.inicializar_db()

# 2. Crear las instancias (Objetos)
moto_honda = Moto("Honda", "CB 190R", 184, 12000000, "Rojo")
moto_yamaha = Moto("Yamaha", "MT-03", 321, 30000000, "Azul")
moto_bmw = Moto("BMW", "S 1000 RR", 999, 110000000, "Negro")
moto_suzuki = Moto("Suzuki", "DR X 250", 249, 23000000, "Amarilla")
moto_kawasaki = Moto("Kawasaki", "Ninja 400", 399, 35000000, "Verde Kawa")
# 3. Probemos la validación (Moto con precio erróneo)
moto_error = Moto("Honda", "Dream Neo", 110, -500000, "Negra")

# 3. Guardar en la DB
db.guardar_moto(moto_honda)
db.guardar_moto(moto_yamaha)
db.guardar_moto(moto_bmw)
db.guardar_moto(moto_suzuki)
db.guardar_moto(moto_kawasaki)
db.guardar_moto(moto_error)


print("¡Datos guardados con una estructura profesional!")