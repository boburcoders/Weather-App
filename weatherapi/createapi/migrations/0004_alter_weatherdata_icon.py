# Generated by Django 5.0.3 on 2024-03-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createapi', '0003_alter_weatherdata_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherdata',
            name='icon',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
