from django.contrib import admin
from .models import AccountingOauth2, FinancialStatementEntryTag, DefaultAccountTagMapping, CoA, CoAMap,TrialBalance
from .forms import CoAForm,CoAMapForm
# Register your models here.


class Oauth2Admin(admin.ModelAdmin):
    list_display = ('company', )
    search_fields = ('company__name',)


class CoAAdmin(admin.ModelAdmin):
    form = CoAForm
    list_display = [field.name for field in CoA._meta.fields]
    search_fields = ('company__name','gl_account_name','gl_account_type',)

class TBAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TrialBalance._meta.fields]
    search_fields = ('company__name', 'gl_account_name',)

class CoAMapAdmin(admin.ModelAdmin):
    form = CoAMapForm
    list_display = [field.name for field in CoAMap._meta.fields]
    search_fields = ('company__name', 'cust_account_name','espresso_account_name')

class DefaultAccountTagMappingAdmin(admin.ModelAdmin):
    list_display = ['softwares','account_category','default_map_id','default_map_name']
    search_fields = ('software','account_category','default_map_id','default_map_name')

    def softwares(self,obj):
        return obj.software.lower()


class FinancialStatementEntryTagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FinancialStatementEntryTag._meta.fields]
    search_fields = ('name', 'all_sight_name')

admin.site.register(AccountingOauth2, Oauth2Admin)
admin.site.register(FinancialStatementEntryTag, FinancialStatementEntryTagAdmin)
admin.site.register(DefaultAccountTagMapping,DefaultAccountTagMappingAdmin)
admin.site.register(CoA, CoAAdmin)
admin.site.register(CoAMap,CoAMapAdmin)
admin.site.register(TrialBalance,TBAdmin)

