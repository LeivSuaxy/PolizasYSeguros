from rest_framework import serializers
from poliza.models import Poliza

class PolizaSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Poliza
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['worker'] = request.user
        return super().create(validated_data)

