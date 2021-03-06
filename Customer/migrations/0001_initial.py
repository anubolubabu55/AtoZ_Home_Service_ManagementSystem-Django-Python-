# Generated by Django 3.1.3 on 2021-03-01 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_id', models.ImageField(upload_to='')),
                ('customer_name', models.CharField(max_length=400)),
                ('customer_phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('customer_address', models.CharField(max_length=500)),
                ('booking_status', models.CharField(max_length=15)),
                ('booking_date', models.DateTimeField(auto_now=True)),
                ('booking_status_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bookings',
            },
        ),
        migrations.CreateModel(
            name='ServiceAreas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=100)),
                ('aregdate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'serviceareas',
            },
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('cregdate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'servicecategory',
            },
        ),
        migrations.CreateModel(
            name='ServicePartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_number', phone_field.models.PhoneField(blank=True, default=99999999, help_text='Contact phone number', max_length=31)),
                ('partner_address', models.CharField(default='Enter the service partner Address', max_length=400)),
                ('partner_image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('partner_category', models.CharField(default='Enter Your Category', max_length=20)),
                ('partner_area', models.CharField(default='Enter Your area', max_length=40)),
                ('partner_validity', models.DateField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'servicepartner',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_id', models.PositiveIntegerField(default=0)),
                ('comments', models.CharField(default='Enter Your Valuable feedback', max_length=1000)),
                ('image', models.ImageField(default='default.jpg', upload_to='feedback_pics')),
                ('rating', models.PositiveIntegerField(default=5)),
                ('booking_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Customer.bookings')),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_number', phone_field.models.PhoneField(blank=True, default=9999999999, help_text='Contact phone number', max_length=31)),
                ('customer_address', models.CharField(default='KLD', max_length=400)),
                ('customer_image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
