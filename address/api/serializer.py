from rest_framework import routers, serializers, viewsets
from address.models import Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        # would restrict fields in full feature applications based on group requirements
        fields = '__all__'
        lookup_fields = ['person_set', 'company_set']
