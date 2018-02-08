(function($) {
    $(function() {
        var AccountType = $('#id_accounting_type'),
            XeroAccountingType = $('.field-xero_accounting_type');


        function toggleVerified(value) {
            value == 'xero' ? XeroAccountingType.show() : XeroAccountingType.hide();
        }

        // show/hide on load based on pervious value of AccountType
        toggleVerified(AccountType.val());

        // show/hide on change
        AccountType.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);