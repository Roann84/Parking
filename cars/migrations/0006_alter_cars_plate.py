# Generated by Django 4.0.3 on 2022-03-29 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_cars_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='plate',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
