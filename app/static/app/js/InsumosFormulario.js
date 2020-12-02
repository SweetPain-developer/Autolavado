$( function () {
    $("#formularioInsumos").validate({
        rules:{
            nombre:{
                required:true,
                minlength:3,
                maxlength:120
            },
            precio:{
                required:true,
            },
        },
        messages:{
            nombre:{
                required:'Ingrese su nombre',
                minlength:'Ingrese un nombre de al menos 3 caracteres',
                maxlength:'nombre ingresado no valido supera 120 caracteres'
            },
            precio:{
                required:'ingrese el precio del producto',
            },
        }
    });
});

$("#ingresar").click(function(){
    if( !$("#formularioInsumos").valid() ) {
        return;
    }
});
