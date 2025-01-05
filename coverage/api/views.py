from common.abstract.apiviews import BaseAdminApiView
# from common.strategy.authpermission import IsAdmin
from coverage.services.coverageservice import CoverageService
from coverage.api.serializer import CoverageSerializerAdmin
from core.guards.permission_classes import IsAdmin

# Create your views here.
class CoverageAdminAPIView(BaseAdminApiView):
    permission_classes = [IsAdmin]
    service = CoverageService()
    cache_key = 'coverages'
    serializer_class = CoverageSerializerAdmin
    object_name_single = 'coverage'
    object_name_many = 'coverages'