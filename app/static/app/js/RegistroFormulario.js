$(function(){
    $("#formularioregistro").validate({
        rules: {
            email:{
                required:true,
                email: true,
            },
            nombre:{
                required:true,
            },
            apellido:{
                required:true,
            },
            usuario:{
                required:true,
            },
            contrasena: {
                required:true,
            },
            fecha:{
                required:true
            }
        },
        messages: {
            nombre:{
                required:'ingrese tu nombre',
            },
            email:{
                required:'ingresa tu correo electronico',
            },
            apellido:{
                required:'ingresa tu apellido',
            },
            usuario:{
                required:'ingresa un nombre de usuario'
            },
            contrasena:{
                required:'ingresa una contraseña'
            },
            fecha:{
                required:'ingrese una fecha de nacimiento'
            }
        }
    });
});

$("#registrate").click(function(){
    if( !$("#formularioRegistro").valid() ) {
        return;
    }
});