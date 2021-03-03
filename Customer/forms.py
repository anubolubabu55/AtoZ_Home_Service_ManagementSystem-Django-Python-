from django import forms
from django.contrib.auth.models import User
from .models import Customer, Feedback, Bookings, ServicePartner, ServiceCategory, ServiceAreas
from django import forms
from django.forms import ModelChoiceField
from django.contrib.auth.forms import UserCreationForm

# This is the form that will be help the admin can add the  New Services
# In this form i am use the only one filed that is Service_category it stores to the ServiceCategory Model
class AddServiceCategoryForm(forms.ModelForm):

    class Meta:
        model = ServiceCategory
        fields = ['category']


# This is the form that will be help the admin can add the  New Area
# In this form i am use the only one filed that is Service_Area it stores to the ServiceAreas Model
class AddServiceAreaForm(forms.ModelForm):
    area = forms.CharField()

    class Meta:
        model = ServiceAreas
        fields = ['area']


class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class CustomerRegistrationForm1(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2','is_staff']
class CustomerUpdationForm(forms.ModelForm):

    class Meta:
        model=Customer
        fields=['customer_number','customer_image','customer_address']

class ServicePartnerRegistraionForm(forms.ModelForm):

    class Meta:
        model=ServicePartner
        fields=['partner_number','partner_address','partner_category','partner_area','partner_validity','partner_image']

class ValidityExtensionForm(forms.ModelForm):

    class Meta:
        model=ServicePartner
        fields=['partner_validity']

class FeedbackForm(forms.ModelForm):

    class Meta:
        model=Feedback
        fields=['comments','image','rating']
