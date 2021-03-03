from django.contrib import admin
from .models import Customer,Feedback,Bookings,ServicePartner,ServiceCategory,ServiceAreas

# Register your models here.

admin.site.register(Customer)
admin.site.register(Feedback)
admin.site.register(Bookings)
admin.site.register(ServicePartner)
admin.site.register(ServiceCategory)
admin.site.register(ServiceAreas)