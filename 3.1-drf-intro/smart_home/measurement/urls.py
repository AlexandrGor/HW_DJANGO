from django.urls import path
from measurement.views import SensorsView, SensorsDetailView, MeasurementsView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<int:pk>/', SensorsDetailView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
]
