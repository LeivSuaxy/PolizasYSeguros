from django.urls import path
from ranges.api.views import RangeAdminAPIView

urlpatterns = [
    path('admin/', RangeAdminAPIView.as_view(), name='range_admin'),
]