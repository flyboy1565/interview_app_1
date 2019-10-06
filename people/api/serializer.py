from rest_framework import routers, serializers, viewsets
from people.models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        # would restrict fields in full feature applications based on group requirements
        fields = '__all__'
