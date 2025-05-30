from django.contrib import admin
from .models import Company, BusinessUnit, Metric, MetricValue

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'sector', 'reporting_period')
    search_fields = ('name', 'sector')

@admin.register(BusinessUnit)
class BusinessUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'company')
    search_fields = ('name',)
    list_filter = ('company',)

@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'year', 'value', 'unit', 'business_unit')
    list_filter = ('category', 'year', 'business_unit__company')
    search_fields = ('name',)

@admin.register(MetricValue)
class MetricValueAdmin(admin.ModelAdmin):
    list_display = ('metric', 'year', 'value', 'unit')
    list_filter = ('year', 'metric__category')
    search_fields = ('metric__name',)