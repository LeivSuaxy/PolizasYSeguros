from django.urls import path
from poliza.api.views import PolizaAdminAPIView

urlpatterns = [
    path('admin/', PolizaAdminAPIView.as_view(), name='poliza_admin'),
]