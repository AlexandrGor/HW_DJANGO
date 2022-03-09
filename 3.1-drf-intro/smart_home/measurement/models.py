from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['-name']
    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='Датчик')
    temperature = models.DecimalField(max_digits=5, decimal_places=1,  verbose_name='Температура')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    image = models.ImageField(null=True, blank=True, verbose_name='Снимок')
    class Meta:
        verbose_name = 'Показание'
        verbose_name_plural = 'Показания'
        ordering = ['-date']
    def __str__(self):
        return str(self.date)