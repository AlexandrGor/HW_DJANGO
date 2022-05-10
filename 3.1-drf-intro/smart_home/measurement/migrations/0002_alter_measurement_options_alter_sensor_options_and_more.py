# Generated by Django 4.0.1 on 2022-03-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'ordering': ['-date'], 'verbose_name': 'Показание', 'verbose_name_plural': 'Показания'},
        ),
        migrations.AlterModelOptions(
            name='sensor',
            options={'ordering': ['-name'], 'verbose_name': 'Датчик', 'verbose_name_plural': 'Датчики'},
        ),
        migrations.AddField(
            model_name='sensor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]