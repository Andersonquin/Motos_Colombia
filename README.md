# 🏍️ Sistema de Inventario - Motos Colombia

Este es un proyecto **Fullstack** diseñado para la gestión de inventarios de motocicletas. Permite visualizar el stock actual desde una base de datos SQLite y registrar nuevos ingresos mediante una interfaz web moderna y organizada.

## 🚀 Características Principales
* **Gestión de Cilindraje:** El sistema permite registrar y visualizar el cilindraje (cc) de cada moto, asegurando datos técnicos precisos.
* **Arquitectura Profesional:** Separación clara de responsabilidades (HTML, CSS, JS y Backend).
* **Validación de Datos:** Uso de Pydantic para garantizar que la información ingresada sea correcta.

## 📋 Estructura del Proyecto
* `api.py`: Servidor FastAPI y rutas de la API.
* `database_manager.py`: Lógica de conexión a SQLite y consultas SQL.
* `main.py`: Script para inicializar la base de datos con datos de prueba.
* `index.html`: Estructura de la interfaz de usuario.
* `style.css`: Diseño visual y estilos (separado para mayor orden).
* `script.js`: Lógica del cliente y comunicación con la API (separado).

## 🛠️ Tecnologías Utilizadas
* **Backend:** Python 3 + FastAPI.
* **Base de Datos:** SQLite 3.
* **Frontend:** HTML5, CSS3 y JavaScript (Fetch API).

## 🔧 Cómo ejecutar el proyecto
1. Instala las dependencias: `pip install -r requirements.txt`.
2. Inicializa la base de datos: `python main.py`.
3. Ejecuta la API: `python -m uvicorn api:app --reload`.
4. Abre `index.html` en tu navegador.