from rest_framework import serializers
from ranges.models import Range

class RangeSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Range
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['worker'] = request.user
        return super().create(validated_data)

