$(function(){
    $("#form-total").steps({
        headerTag: "h2",
        bodyTag: "section",
        transitionEffect: "fade",
        enableAllSteps: true,
        autoFocus: true,
        transitionEffectSpeed: 500,
        titleTemplate : '<div class="title">#title#</div>',
        labels: {
            previous : 'Back',
            next : 'Siguiente',
            finish : 'Confirmar',
            current : ''
        },
        onStepChanging: function (event, currentIndex, newIndex) { 
            var fullname = $('#first_name').val() + ' ' + $('#last_name').val();
            var litros = $('#litros').val();
            var direccion = $('#calle').val()+ ' ' + $('#num_ext').val() + ' ' + $('#num_int').val();
            var dir_2 = $('#cp').val() + ' ' + $('#ciudad').val() + ' ' + $('#colonia').val();
           
            $('#fullname-val').text(fullname);
            $('#litros-val').text(litros);
            $('#direccion-val').text(direccion);
            $('#dir_2-val').text(dir_2);
            

            return true;
        }
    });
    $("#day").datepicker({
        dateFormat: "MM - DD - yy",
        showOn: "both",
        buttonText : '<i class="zmdi zmdi-chevron-down"></i>',
    });
});
