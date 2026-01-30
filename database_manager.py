import sqlite3

class DatabaseManager:
    def __init__(self, db_name="concesionario_motos.db"):
        self.db_name = db_name

    def inicializar_db(self):
        try:
            with sqlite3.connect(self.db_name) as conexion:
                cursor = conexion.cursor()
                # Borramos la tabla anterior para aplicar los nuevos cambios de estructura
                cursor.execute("DROP TABLE IF EXISTS Motos")
                cursor.execute("""
                    CREATE TABLE Motos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        marca TEXT NOT NULL,
                        referencia TEXT NOT NULL,
                        cilindraje INTEGER NOT NULL,
                        precio REAL NOT NULL,
                        color TEXT NOT NULL
                    )
                """)
                print("Base de datos inicializada con la columna CILINDRAJE.")
        except sqlite3.Error as e:
            print(f"Error al inicializar la DB: {e}")

    def guardar_moto(self, moto):
        try:
            with sqlite3.connect(self.db_name) as conexion:
                cursor = conexion.cursor()
                # Añadimos el cilindraje tanto en la consulta como en los valores
                cursor.execute("""
                    INSERT INTO Motos (marca, referencia, cilindraje, precio, color) 
                    VALUES (?, ?, ?, ?, ?)
                """, (moto.marca, moto.referencia, moto.cilindraje, moto.precio, moto.color))
                conexion.commit() 
        except sqlite3.Error as e:
            print(f"Error al guardar la moto: {e}")

    def obtener_todas_las_motos(self):
        try:
            with sqlite3.connect(self.db_name) as conexion:
                conexion.row_factory = sqlite3.Row 
                cursor = conexion.cursor()
                # El SELECT * traerá automáticamente la nueva columna
                cursor.execute("SELECT * FROM Motos")
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error al leer la DB: {e}")
            return []