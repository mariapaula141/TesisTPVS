//Base
$(function() {
     $('#sidebarCollapse').on('click', function () {
                     $('#sidebar').toggleClass('active');
                 });
});

//TABLAS===========
$(function() {

        var data;
        var table=$('#tables').DataTable({
            
            "language": {
                "url": "//cdn.datatables.net/plug-ins/1.10.16/i18n/Spanish.json"
            }
        } );
        $('#tablesDtm').DataTable({
         
            "language": {
                "url": "//cdn.datatables.net/plug-ins/1.10.16/i18n/Spanish.json"
            }
        } );
       $('#tables tbody').on( 'click', 'tr', function () {
            if ( $(this).hasClass('selected') ) {
                $(this).removeClass('selected');
            }
            else {
                table.$('tr.selected').removeClass('selected');
                $(this).addClass('selected');
            }
            data = table.row( this ).data();            document.getElementById("inputId").value = data[0];
            location.hash ="top";
        } );

       
   
});

//Boton

$('.carga').on('click', function() {
    var $this = $(this);
  $this.button('Cargando');
    setTimeout(function() {
       $this.button('reset');
   }, 8000);
});

