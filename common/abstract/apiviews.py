from rest_framework.views import APIView
from common.abstract.service import BaseService
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from common.utils.cache_utils import delete_cache

class BaseAdminApiView(APIView):
    """
        Abstract class for management views.

        REQUIRED VARIABLES:
        - permission_classes: List of permission classes required to access the view.
        - service: Instance of the service that handles the business logic.
        - cache_key: Key used to store and retrieve data in the cache.
        - object_name_many: Plural name of the object, used in response messages.
        - object_name_single: Name of the object in singular, used in response messages.
        - serializer_class: Serializer class used to validate and transform data.
    """

    permission_classes = []
    service: BaseService | object = None
    cache_key: str = None
    object_name_many: str = None
    object_name_single: str = None
    serializer_class: ModelSerializer = None

    def get(self, request):
        if cache.get(self.cache_key):
            return Response(cache.get(self.cache_key), status=status.HTTP_200_OK)

        data = self.service.get_all()
        if not data:
            return Response({'message': f'There are not {self.object_name_many} in database'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        delete_cache(self.cache_key)

        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        delete_cache(self.cache_key)

        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)