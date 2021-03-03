from django.shortcuts import render,redirect
from Customer.forms import CustomerRegistrationForm,CustomerUpdationForm,ServicePartnerRegistraionForm,\
                   FeedbackForm,AddServiceAreaForm,AddServiceCategoryForm
from django.contrib import messages
from django.contrib.auth.models import User
from Customer.models import Customer, Feedback, Bookings, ServicePartner, ServiceCategory, ServiceAreas

# Create your views here.
def index(request):
    if request.method == 'POST':
        id=request.user.id
        user = User.objects.get(id=id)
        customer=Customer.objects.get(user_id=id)
        context={
            'user':user,
            'customer':customer
        }
        return render(request,'ServicePartner/index.html',context)
    else:
        return render(request, 'ServicePartner/index.html')
