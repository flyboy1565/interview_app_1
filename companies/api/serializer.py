from rest_framework import routers, serializers, viewsets
from companies.models import Company

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        # would restrict fields in full feature applications based on group requirements
        fields = '__all__'