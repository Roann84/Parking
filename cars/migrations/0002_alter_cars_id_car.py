# Generated by Django 4.0.3 on 2022-03-26 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='id_car',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
