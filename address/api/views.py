from rest_framework import routers, serializers, viewsets
from address.models import Address

from .serializer import AddressSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
