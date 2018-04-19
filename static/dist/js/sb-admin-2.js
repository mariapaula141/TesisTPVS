//Base
$(function() {
     $('#sidebarCollapse').on('click', function () {
                     $('#sidebar').toggleClass('active');
                 });
});

//Trader
$(function() {
      $('#tables').DataTable({
                    "language": {
                        "url": "//cdn.datatables.net/plug-ins/1.10.16/i18n/Spanish.json"
                    }
                } );
       $('#tablesDtm').DataTable({
                    "language": {
                        "url": "//cdn.datatables.net/plug-ins/1.10.16/i18n/Spanish.json"
                    }
                } );
    
});
