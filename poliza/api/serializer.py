from poliza.models import Poliza
from common.serializers.base import BaseSerializerAdmin

class PolizaSerializerAdmin(BaseSerializerAdmin):
    model = Poliza
    admin_permission = 'admin'

