# Generated by Django 4.0.3 on 2022-03-28 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_cars_left_alter_cars_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='time',
            field=models.CharField(default=False, max_length=255),
        ),
    ]
