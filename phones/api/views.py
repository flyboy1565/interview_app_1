from rest_framework import routers, serializers, viewsets
from phones.models import Phone
from .serializer import PhoneSerializer

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
