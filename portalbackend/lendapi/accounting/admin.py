from django.contrib import admin
from .models import AccountingOauth2, FinancialStatementEntryTag, DefaultAccountTagMapping, CoA, CoAMap,TrialBalance
from .forms import CoAForm,CoAMapForm
# Register your models here.


class Oauth2Admin(admin.ModelAdmin):
    list_display = ('company', )


class CoAAdmin(admin.ModelAdmin):
    form = CoAForm
    list_display = [field.name for field in CoA._meta.fields]

class CoAMapAdmin(admin.ModelAdmin):
    form = CoAMapForm

class FinancialStatementEntryTagAdmin(admin.ModelAdmin):
    list_display = ('short_label', 'description', 'tag_id', 'sort_order')

admin.site.register(AccountingOauth2, Oauth2Admin)
admin.site.register(FinancialStatementEntryTag, FinancialStatementEntryTagAdmin)
admin.site.register(DefaultAccountTagMapping)
admin.site.register(CoA, CoAAdmin)
admin.site.register(CoAMap,CoAMapAdmin)
admin.site.register(TrialBalance)

