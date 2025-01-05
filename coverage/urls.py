from django.urls import path
from coverage.api.views import CoverageAdminAPIView

urlpatterns = [
    path('admin/', CoverageAdminAPIView.as_view(), name='coverage_admin'),
]