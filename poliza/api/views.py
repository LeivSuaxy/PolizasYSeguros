from poliza.api.serializer import PolizaSerializerAdmin
from poliza.services.polizaservice import PolizaService
from common.abstract.apiviews import BaseAdminApiView
from core.guards.permission_classes import IsAdmin


# Create your views here.
class PolizaAdminAPIView(BaseAdminApiView):
    permission_classes = [IsAdmin]
    service = PolizaService()
    cache_key = 'polizas'
    serializer_class = PolizaSerializerAdmin
    object_name_single = 'poliza'
    object_name_many = 'polizas'