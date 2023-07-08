function guardar() {
    let n = document.getElementById("nombre").value
    let c = parseInt(document.getElementById("cantidad").value)
    let d = document.getElementById("direccion").value

    // {
    //     "imagen": "https://picsum.photos/200/300?grayscale",
    //     "nombre": "MICROONDAS",
    //     "precio": 50000,
    //     "stock": 10
    //   }

    let producto = {
        nombre: n,
        cantidad: c,
        direccion: d,
    }
    let url = "http://localhost:5000/productos"
    var options = {
        body: JSON.stringify(producto),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
            // Devuelve el href (URL) de la página actual
            window.location.href = "compras.html";
            
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}