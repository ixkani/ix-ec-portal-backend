(function($) {
    $(function() {
        var AccountType = $('#id_accounting_type'),
            XeroAccountingType = $('.field-type');


        function toggleVerified(value) {
            value == 'Xero' ? XeroAccountingType.show() : XeroAccountingType.hide();
        }

        // show/hide on load based on pervious value of AccountType
        toggleVerified(AccountType.val());

        // show/hide on change
        AccountType.change(function() {
            toggleVerified($(this).val());
        });

        $('#id_is_tfa_setup_completed').attr('disabled','disabled');

        $( "input[name='enforce_tfa_enabled']" ).on( "click", function(){
            var is_tfa_enabled = $( "input[name='is_tfa_enabled']:checked" ).length;
            if(!is_tfa_enabled){
                $('#id_is_tfa_setup_completed').prop("checked", false);
            }
        } );

        $( "input[name='is_tfa_enabled']" ).on( "click", function(){
            var enforce_flag = $( "input[name='enforce_tfa_enabled']:checked" ).length;
            var setup_flag = $( "input[name='is_tfa_setup_completed']:checked" ).length;
            if(!enforce_flag){
                if(setup_flag){
                     $('#id_is_tfa_setup_completed').prop("checked", false);
                }
            }
        } );
    });



})(django.jQuery);