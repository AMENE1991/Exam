from rest_framework.serializers import ModelSerializer
from AutoRu.models import Vehicle

class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'