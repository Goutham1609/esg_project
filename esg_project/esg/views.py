from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Company, BusinessUnit, Metric, MetricValue, CustomUser
from .serializers import (
    CompanySerializer,
    BusinessUnitSerializer,
    MetricSerializer,
    MetricValueSerializer
)
from .services import get_company_metrics_summary
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .permissions import IsAdmin, IsManager, IsViewer


def api_home(request):
    return JsonResponse({"message": "Welcome to the ESG API!"})


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.create_user(
                username=request.data['username'],
                password=request.data['password'],
                email=request.data.get('email', ''),
                role=request.data.get('role', 'viewer')
            )
            return Response({"message": "User registered successfully."}, status=201)
        return Response(serializer.errors, status=400)
    

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'sector']
    permission_classes = [IsManager]

    @action(detail=True, methods=['get'], url_path='metrics-summary')
    def metrics_summary(self, request, pk=None):
        summary = get_company_metrics_summary(pk)
        if not summary:
            return Response({"detail": "Company not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(summary)
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsViewer()]
        return [IsManager()]

class BusinessUnitViewSet(viewsets.ModelViewSet):
    queryset = BusinessUnit.objects.all()
    serializer_class = BusinessUnitSerializer

class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'category']
    ordering_fields = ['year', 'category']

class MetricValueViewSet(viewsets.ModelViewSet):
    queryset = MetricValue.objects.all()
    serializer_class = MetricValueSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['metric__name', 'year']
    ordering_fields = ['year', 'metric']

class CompanyMetricsSummaryView(APIView):
    def get(self, request, company_id):
        summary = get_company_metrics_summary(company_id)
        if not summary:
            return Response({"detail": "Company not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(summary)