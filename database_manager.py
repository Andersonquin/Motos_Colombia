import sqlite3

class DatabaseManager:
    def __init__(self, db_name="concesionario_motos.db"):
        self.db_name = db_name

    def inicializar_db(self):
        try:
            with sqlite3.connect(self.db_name) as conexion:
                cursor = conexion.cursor()
                cursor.execute("DROP TABLE IF EXISTS Motos")
                cursor.execute("""
                    CREATE TABLE Motos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        marca TEXT,
                        referencia TEXT,
                        precio REAL,
                        color TEXT
                    )
                """)
                print("Base de datos inicializada correctamente.")
        except sqlite3.Error as e:
            print(f"Error al inicializar la DB: {e}")

    def guardar_moto(self, moto):
        try:
            with sqlite3.connect(self.db_name) as conexion:
                cursor = conexion.cursor()
                # Usamos parámetros (?) para evitar inyección SQL (esto ya lo haces bien)
                cursor.execute("""
                    INSERT INTO Motos (marca, referencia, precio, color) 
                    VALUES (?, ?, ?, ?)
                """, (moto.marca, moto.referencia, moto.precio, moto.color))
                # No hace falta conexion.commit() manual con 'with' en algunas versiones, 
                # pero ponerlo asegura la transacción.
                conexion.commit() 
        except sqlite3.Error as e:
            print(f"Error al guardar la moto: {e}")

    def obtener_todas_las_motos(self):
        try:
            with sqlite3.connect(self.db_name) as conexion:
                # Esto permite que los resultados se comporten como diccionarios
                conexion.row_factory = sqlite3.Row 
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM Motos")
                # Convertimos las filas en una lista de diccionarios para JSON
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error al leer la DB: {e}")
            return []