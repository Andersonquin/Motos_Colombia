# Archivo: main.py
from database_manager import DatabaseManager
from api import Moto  # Importamos el modelo oficial para que los campos coincidan

def cargar_datos_iniciales():
    # 1. Instanciar el manejador
    db = DatabaseManager()

    # 2. Limpiar y crear la tabla con la nueva columna 'cilindraje'
    print("Borrando tabla antigua y creando la nueva con cilindraje...")
    db.inicializar_db()

    # 3. Crear los objetos Moto
    # Nota: Pydantic ahora valida que uses: marca, referencia, cilindraje, precio, color
    motos_para_guardar = [
        Moto(marca="Honda", referencia="CB 190R", cilindraje=184, precio=12000000, color="Rojo"),
        Moto(marca="Yamaha", referencia="MT-03", cilindraje=321, precio=30000000, color="Azul"),
        Moto(marca="BMW", referencia="S 1000 RR", cilindraje=999, precio=110000000, color="Negro"),
        Moto(marca="Suzuki", referencia="DR X 250", cilindraje=249, precio=23000000, color="Amarilla"),
        Moto(marca="Kawasaki", referencia="Ninja 400", cilindraje=399, precio=35000000, color="Verde Kawa")
    ]

    # 4. Guardar en la DB usando un ciclo (más limpio que repetir la línea 5 veces)
    print("Guardando motos en el inventario...")
    for moto in motos_para_guardar:
        db.guardar_moto(moto)

    print("¡Base de datos preparada con éxito!")

if __name__ == "__main__":
    cargar_datos_iniciales()