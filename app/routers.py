from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns

from people.api.views import PersonViewSet
from companies.api.views import CompanyViewSet
from address.api.views import AddressViewSet
from phones.api.views import PhoneViewSet


router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'address', AddressViewSet)
router.register(r'phone', PhoneViewSet)