from rest_framework import routers, serializers, viewsets
from phones.models import Phone

class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phone
        # would restrict fields in full feature applications based on group requirements
        fields = '__all__'
