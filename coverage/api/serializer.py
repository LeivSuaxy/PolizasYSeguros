from rest_framework import serializers
from coverage.models import Coverage

class CoverageSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Coverage
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['worker'] = request.user
        return super().create(validated_data)

