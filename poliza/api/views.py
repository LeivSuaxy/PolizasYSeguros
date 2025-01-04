from common.strategy.authpermission import IsAdmin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.strategy.authpermission import IsAdmin
from common.utils.cache_utils import delete_cache
from poliza.api.serializer import PolizaSerializerAdmin
from poliza.services.polizaservice import PolizaService
from django.core.cache import cache


# Create your views here.
class PolizaAdminAPIView(APIView):
    permission_classes = [IsAdmin]
    service = PolizaService()
    cache_key = 'polizas'

    def get(self, request):
        if cache.get(self.cache_key):
            return Response(cache.get(self.cache_key), status=status.HTTP_200_OK)

        polizas = self.service.get_all()
        if not polizas:
            return Response({'message': "There are not polizas in database"} ,status=status.HTTP_404_NOT_FOUND)

        serializer = PolizaSerializerAdmin(polizas, many=True)
        cache.set(self.cache_key, serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        delete_cache(self.cache_key)

        serializer = PolizaSerializerAdmin(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        delete_cache(self.cache_key)

        poliza = self.service.get_by_id(request.data['id'])
        if poliza is None:
            return Response({'message': 'Poliza not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PolizaSerializerAdmin(poliza, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        delete_cache(self.cache_key)

        poliza = self.service.get_by_id(request.data['id'])
        if poliza is None:
            return Response({'message': 'Poliza not found'}, status=status.HTTP_404_NOT_FOUND)

        poliza.delete()
        return Response({'message': 'Poliza deleted successfully'}, status=status.HTTP_200_OK)

