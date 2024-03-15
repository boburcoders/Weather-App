# Generated by Django 5.0.3 on 2024-03-13 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=30)),
                ('pressure', models.FloatField()),
                ('temperature', models.FloatField()),
                ('description', models.CharField(max_length=40)),
                ('icon', models.ImageField(upload_to='media/weather_icon')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
    ]
