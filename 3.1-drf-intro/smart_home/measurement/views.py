from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, CreateAPIView
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer
from .models import Sensor, Measurement

class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorsDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementsView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer