from django.contrib import admin
from .models import AccountingOauth2, FinancialStatementEntryTag, DefaultAccountTagMapping, CoA, CoAMap,TrialBalance
from .forms import CoAForm,CoAMapForm
# Register your models here.


class Oauth2Admin(admin.ModelAdmin):
    list_display = ('company', )


class CoAAdmin(admin.ModelAdmin):
    form = CoAForm
    list_display = [field.name for field in CoA._meta.fields]

class TBAdmin(admin.ModelAdmin):

    list_display = [field.name for field in TrialBalance._meta.fields]

class CoAMapAdmin(admin.ModelAdmin):
    form = CoAMapForm
    list_display = [field.name for field in CoAMap._meta.fields]

class DefaultAccountTagMappingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DefaultAccountTagMapping._meta.fields]

class FinancialStatementEntryTagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FinancialStatementEntryTag._meta.fields]

admin.site.register(AccountingOauth2, Oauth2Admin)
admin.site.register(FinancialStatementEntryTag, FinancialStatementEntryTagAdmin)
admin.site.register(DefaultAccountTagMapping,DefaultAccountTagMappingAdmin)
admin.site.register(CoA, CoAAdmin)
admin.site.register(CoAMap,CoAMapAdmin)
admin.site.register(TrialBalance,TBAdmin)

