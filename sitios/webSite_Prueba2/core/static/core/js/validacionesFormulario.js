$(function() {
    $("#formulario").validate( {
        rules:
        {
            rut:
            {
                required: true,
                minlength: 9,
                maxlength: 10

            },
            nombre:
            {
                required: true,
                minlength: 10,
                maxlength: 60
            },
            edad:
            {
                required: true,
                minlength: 1,
                digits: true,
                maxlength: 3
            },
            region:
            {
                required: true
            },
            codPostal:
            {
                required: true,
                minlength: 6,
                maxlength: 6,
                digits: true
            },
            correo:
            {
                required: true,
                minlength: 10,
                maxlength: 100
            },
            contraseña:
            {
                required: true,
                minlength: 8,
                maxlength: 20
            },
            conf_contra:
            {
                 required: true,
                 equalTo: "#contraseña"
            },
            fecha:
            {
                required: true
            },
            preferencia:
            {
                required: true
            },

        },
        messages:
        {
            rut:
            {
                required:"Tienes que ingresar tu rut."
            },
            nombre:
            {
                required:"Tienes que ingresar tu nombre y apellido.",
                minlength:"Tienes que ingresar como mínimo 2 caracteres.",
                maxlength:"Puedes ingresar como máximo de 30 caracteres."
            },
            edad:
            {
                required:"Tienes que ingresar tu edad.",
                minlength:"Como mínimo tienes que ingresar un dígito.",
                maxlength:"Como máximo puedes ingresar 3 dígitos como máximo."
            },
            codPostal:
            {
                required:"Tienes que ingresar un código postal."
            },
            correo:
            {
                required:"Tienes que ingresar tu correo electrónico.",
                email:"El formato no es de una dirección de correo.",
                minlength:"Tienes que ingresar un correo válido.",
                maxlength:"Tu correo excede el largo máximo permitido."
            },
            contraseña:
            {   
                required:"Tienes que ingresar tu contraseña.",
                minlength:"Como mínimo tienes que ingresar 8 caracteres.",
                maxlength:"Como máximo puedes ingresar 20 caracteres."
            },
            conf_contra:
            {
                required:"Tienes que confirmar tu contraseña.",
                minlength:"Como mínimo tienes que ingresar 8 caracteres.",
                maxlength:"Como máximo puedes ingresar 20 caracteres.",
                equalTo:"Las contraseñas no coinciden."
            },
            fecha:
            {
                required:"Tienes que ingresar tu fecha de nacimiento"
            },
            preferencia:
            {
                required:"Por favor, déjanos tus comentarios."
            },
            confirmar:
            {
                required:"Debe aceptar los términos y condiciones antes de registrarse."
            }    
        }
    });
});