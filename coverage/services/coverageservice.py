from common.abstract.service import BaseService
from coverage.models import Coverage

class CoverageService(BaseService):
    model = Coverage