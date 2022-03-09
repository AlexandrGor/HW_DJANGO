from rest_framework import serializers
from .models import Sensor, Measurement

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description',]

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensor', 'temperature', 'date', 'image']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements',]
