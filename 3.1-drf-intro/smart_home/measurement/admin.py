from django.contrib import admin
from .models import Sensor, Measurement

class MeasurementInline(admin.TabularInline):
    model = Measurement
    readonly_fields = ('temperature','date','image')
    can_delete = False
    extra = 0

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    inlines = [MeasurementInline, ]

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
