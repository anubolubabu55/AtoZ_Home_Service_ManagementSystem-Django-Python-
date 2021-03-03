from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.utils.timezone import now
from phone_field import PhoneField


# This Model for the Service Areas provided by the AtoZ
# Here i am declare the area and registration_date these two are the fields
class ServiceAreas(models.Model):
    area = models.CharField(max_length=100)
    aregdate = models.DateTimeField(auto_now=True)
    class Meta:
        db_table="serviceareas"

# This Model for the Service Category provided by the AtoZ
# Here i am declare the category and registration_date these two are the fields
class ServiceCategory(models.Model):
    category = models.CharField(max_length=200)
    cregdate = models.DateTimeField(auto_now=True)
    class Meta:
        db_table="servicecategory"


# This Model for the General User Account Extra Fields
# Here i am declare the customer_phone_number,address,image are the fields
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_number=PhoneField(blank=True, help_text='Contact phone number',default=9999999999)
    customer_address=models.CharField(max_length=400,default="KLD")
    customer_image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    class Meta:
        db_table="customer"

    def __str__(self):
        return "%s customer" % self.user.id

def create_customer(sender, instance, created, **kwargs):
    if created:
        customer,created = Customer.objects.get_or_create(user=instance)

post_save.connect(create_customer, sender=User)

# This Model for the Service Partner Account Extra Fields
# Here i am declare the Service Partner Mobilenumber,Image,Address,Category,City,Validation dates
class ServicePartner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    partner_number = PhoneField(blank=True, help_text='Contact phone number',default=99999999)
    partner_address = models.CharField(max_length=400,default="Enter the service partner Address")
    partner_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    partner_category=models.CharField(max_length=20,default="Enter Your Category")
    partner_area=models.CharField(max_length=40,default="Enter Your area")
    partner_validity=models.DateField(null=True)
    class Meta:
        db_table="servicepartner"

        def __str__(self):
            return "%s's partner" % self.user.id

def create_service_partner(sender, instance, created, **kwargs):
    if created:
        service_partner,created = ServicePartner.objects.get_or_create(user=instance)

post_save.connect(create_service_partner, sender=User)


# This Model for the Bookings Tracking
# Here i am declare the booking_id,partner_id,customer_name,user_name,Customer_phonenumber,Customer Address,
# and the service status , service time
class Bookings(models.Model):
    partner_id=models.IntegerField()
    customer_name=models.CharField(max_length=400)
    customer_phone=PhoneField(blank=True, help_text='Contact phone number')
    customer_address=models.CharField(max_length=500)
    booking_status=models.CharField(max_length=15)
    booking_date=models.DateTimeField(default=datetime.now, editable=False)
    booking_status_date=models.DateTimeField(default=datetime.now, editable=True)
    class Meta:
        db_table="bookings"



# This is the model for the Feedback
# In this model i am using the booking id,provider_id,comments,Service_experience fields
class Feedback(models.Model):
    booking_id=models.OneToOneField(Bookings,on_delete=models.CASCADE)
    provider_id=models.PositiveIntegerField(default=000)
    comments=models.CharField(max_length=1000,default="Enter Your Valuable feedback")
    image=models.ImageField(upload_to='feedback_pics',default="default.jpg")
    rating=models.PositiveIntegerField(default=5)
    class Meta:
        db_table="feedback"
