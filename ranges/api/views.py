from common.abstract.apiviews import BaseAdminApiView
from ranges.api.serializer import RangeSerializerAdmin
from ranges.services.rangeservice import RangeService
from core.guards.permission_classes import IsAdmin

# Create your views here.
class RangeAdminAPIView(BaseAdminApiView):
    permission_classes = [IsAdmin]
    service = RangeService()
    cache_key = 'ranges'
    serializer_class = RangeSerializerAdmin
    object_name_single = 'range'
    object_name_many = 'ranges'