# Generated by Django 3.1.3 on 2021-03-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_auto_20210301_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='partner_id',
            field=models.IntegerField(max_length=100),
        ),
    ]
