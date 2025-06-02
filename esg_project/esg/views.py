from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Company, BusinessUnit, Metric, MetricValue
from .serializers import (
    CompanySerializer,
    BusinessUnitSerializer,
    MetricSerializer,
    MetricValueSerializer
)
from .services import get_company_metrics_summary

def home(request):
    return HttpResponse("Welcome to the ESG API!")
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'], url_path='metrics-summary')
    def metrics_summary(self, request, pk=None):
        summary = get_company_metrics_summary(pk)
        if not summary:
            return Response({"detail": "Company not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(summary)

class BusinessUnitViewSet(viewsets.ModelViewSet):
    queryset = BusinessUnit.objects.all()
    serializer_class = BusinessUnitSerializer

class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

class MetricValueViewSet(viewsets.ModelViewSet):
    queryset = MetricValue.objects.all()
    serializer_class = MetricValueSerializer