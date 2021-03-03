from django.shortcuts import render,redirect
from .forms import CustomerRegistrationForm,CustomerUpdationForm,ServicePartnerRegistraionForm,\
                   FeedbackForm,AddServiceAreaForm,AddServiceCategoryForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Customer, Feedback, Bookings, ServicePartner, ServiceCategory, ServiceAreas
from django.db.models import Q
from django.shortcuts import get_object_or_404

# Create your views here.
def person(request):
    book=Bookings.objects.filter(customer_name=request.user.username)
    context = {
        'book':book
    }
    return render(request, 'person.html', context)

def index(request):
    return render(request, 'index.html')

# This View About Information of Web Developers and others
def about(request):
    return render(request,'about.html')

# This View For Show the providing services of the AtoZ
def services(request):
    return render(request,'services.html')

#This View for the Find The Professionals based on the requirement
def find_professionls(request):
    if request.method=='POST':
        category1=request.POST.get('category')
        area1 = request.POST.get('city')
        partner=get_object_or_404(ServicePartner,partner_category=category1, partner_area=area1)
        context = {
            'partner':partner
        }
        return render(request, 'find_professionals.html', context)

    else:
        return render(request,'find_professionals.html')

def book(request,id):

    customer_name=request.user.username
    customer=Customer.objects.get(id=request.user.id)
    customer_phone=customer.customer_number
    customer_address=customer.customer_address

    book=Bookings.objects.create(partner_id=id, customer_name=customer_name, customer_phone=customer_phone,
                                 customer_address=customer_address,booking_status="Receive")
    book.save()
    return redirect('person')

#This View For User LOGIN to Book the Service Partner
def login(request):
    return render(request,'login.html')

#This View for Customer Account Registration
def user_registration(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For {username}')
            return redirect('user_add_more')
        else:
            messages.error(request, f'Some Thing Went wrong in 2 !!!')
            return redirect("user_registration")
    else:
        form = CustomerRegistrationForm()
        context={
            'form':form,
                    }
        return render(request, 'user_registration.html',context)

def user_add_more(request):
    user=User.objects.latest('id')
    id=user.id
    customer=Customer.objects.get(user_id=id)
    if request.method == "POST":
        form = CustomerUpdationForm(request.POST, instance=customer)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('../login')
    else:
        form = CustomerUpdationForm(instance=customer)
        return render(request, 'user_update.html', {'form': form})


#This view for the contact information about the AoZ Providers
def contact(request):
    return render(request,'contact.html')

#This View for The Feedback of the Employees of the first 10 members
def feedback(request):
    return render(request,'feedback.html')


