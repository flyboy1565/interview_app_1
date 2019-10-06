from rest_framework import routers, serializers, viewsets
from companies.models import Company

from .serializer import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer