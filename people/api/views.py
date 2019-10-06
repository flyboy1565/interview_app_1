from rest_framework import routers, serializers, viewsets
from people.models import Person

from .serializer import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
