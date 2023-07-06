document.formularioo.addEventListener('submit', validarFormulario);
function validarFormulario(evObject) {
evObject.preventDefault();}
function validarFormulario(){
    var nombre = document.getElementById("firstname").value.trim();
      var apellido = document.getElementById("lastname").value.trim();
      var telefono = document.getElementById("telefono").value.trim();
      var mail = document.getElementById("mail").value.trim();
      var mensaje = document.getElementById("message-input").value.trim();
      const botonEnviar = document.getElementById('botonenviar');
  
      if (nombre == "" || apellido == "" || telefono == "" || mail == "" || mensaje == "") {
          alert("No pueden quedar espacios en blanco.");
          return false;}

            for (var i = 0; i < nombre.length; i++) {
                var charCode = nombre.charCodeAt(i);
                if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122) || charCode === 32)) {
                alert("El campo 'nombre' solo puede contener caracteres alfabéticos y espacios.");return false; }}

            for (var i = 0; i < apellido.length; i++) {
            var charCode = apellido.charCodeAt(i);
            if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122) || charCode === 32)) {
            alert("El campo 'apellido' solo puede contener caracteres alfabéticos y espacios.");return false; }}

            if( isNaN(telefono) ) {
                alert("El campo 'teléfono' solo admite números.")
                return false;
              }

  
          alert("Formulario enviado correctamente.");
          return true;
    }


    
        

    
  
