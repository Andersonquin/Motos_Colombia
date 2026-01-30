const API_URL = 'http://127.0.0.1:8000/motos';

// Función para pedir las motos a la API
async function cargarMotos() {
    try {
        const respuesta = await fetch(API_URL);
        const datos = await respuesta.json();
        const contenedor = document.getElementById('motos-lista');
        contenedor.innerHTML = ''; 

        datos.motos.forEach(moto => {
            contenedor.innerHTML += `
                <div class="card">
                    <h3>${moto.marca}</h3>
                    <p><strong>Ref:</strong> ${moto.referencia}</p>
                    <span class="cilindraje-tag">${moto.cilindraje} cc</span>
                    <span class="precio">$${moto.precio.toLocaleString()}</span>
                    <p class="color-text">Color: ${moto.color}</p>
                </div>
            `;
        });
    } catch (error) {
        console.error("Error al cargar motos:", error);
    }
}

// Función para enviar una nueva moto
document.getElementById('form-moto').addEventListener('submit', async (e) => {
    e.preventDefault();
    const nuevaMoto = {
        marca: document.getElementById('marca').value,
        referencia: document.getElementById('referencia').value,
        cilindraje: parseInt(document.getElementById('cilindraje').value),
        precio: parseFloat(document.getElementById('precio').value),
        color: document.getElementById('color').value
    };

    try {
        const respuesta = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(nuevaMoto)
        });

        if (respuesta.ok) {
            e.target.reset();
            cargarMotos();
        }
    } catch (error) {
        alert("Error de conexión con el servidor");
    }
});

// Cargar al iniciar
window.onload = cargarMotos;