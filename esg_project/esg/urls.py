from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, BusinessUnitViewSet, MetricViewSet, MetricValueViewSet, CompanyMetricsSummaryView

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'business-units', BusinessUnitViewSet)
router.register(r'metrics', MetricViewSet)
router.register(r'metric-values', MetricValueViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/company-metrics-summary/<int:company_id>/', CompanyMetricsSummaryView.as_view(), name='company_metrics_summary'),
]
