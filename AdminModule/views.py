from django.shortcuts import render, redirect
from Customer.forms import CustomerRegistrationForm1, CustomerUpdationForm,ValidityExtensionForm, ServicePartnerRegistraionForm,FeedbackForm, AddServiceAreaForm, AddServiceCategoryForm
from django.contrib import messages
from django.contrib.auth.models import User
from Customer.models import Customer, Feedback, Bookings, ServicePartner, ServiceCategory, ServiceAreas



# Create your views here.
def index(request):
    if request.method == 'POST':
        id = request.user.id
        user = User.objects.get(id=id)
        customer = Customer.objects.get(user_id=id)
        context = {
            'user': user,
            'customer': customer
        }
        return render(request, 'AdminModule/index.html', context)
    else:
        return render(request, 'AdminModule/index.html')


def add_category(request):
    if request.method=='POST':
        form=AddServiceCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_category')
        else:
            return redirect('add_category')
    else:
        form=AddServiceCategoryForm()
        context={
            'form': form
        }
        return render(request, 'AdminModule/add_category.html', context)

def view_category(request):
    category=ServiceCategory.objects.all()
    return render(request,'AdminModule/view_category.html',{'category':category})

def edit_category(request,id):
    category=ServiceCategory.objects.get(id=id)
    if request.method=='POST':
        form=AddServiceCategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('view_category')
    else:
        form=AddServiceCategoryForm(instance=category)
        context={
            'form': form
        }
        return render(request, 'AdminModule/edit_category.html', context)

def delete_category(request,id):
    category=ServiceCategory.objects.get(id=id)
    if request.method=='POST':
        category.delete()
        return redirect('view_category')
    else:

        context={
                'category':category
                   }
        return render(request, 'AdminModule/delete_category.html', context)

def add_area(request):
    if request.method=='POST':
        form=AddServiceAreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_area')
        else:
            return redirect('add_area')
    else:
        form=AddServiceAreaForm()
        context={
            'form': form
        }
        return render(request, 'AdminModule/add_area.html', context)

def view_area(request):
    area=ServiceAreas.objects.all()
    return render(request,'AdminModule/view_area.html',{'area':area})

def edit_area(request,id):
    area=ServiceAreas.objects.get(id=id)
    if request.method=='POST':
        form=AddServiceAreaForm(request.POST,instance=area)
        if form.is_valid():
            form.save()
            return redirect('view_area')
    else:
        form=AddServiceAreaForm(instance=area)
        context={
            'form': form
        }
        return render(request, 'AdminModule/edit_area.html', context)

def delete_area(request,id):
    area=ServiceAreas.objects.get(id=id)
    if request.method=='POST':
        area.delete()
        return redirect('view_area')
    else:

        context={
                'area':area
                   }
        return render(request, 'AdminModule/delete_area.html', context)

def add_partner(request):
    if request.method == "POST":
        form = CustomerRegistrationForm1(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For {username}')
            return redirect('partner_add_more')
        else:
            messages.error(request, f'Some Thing Went wrong in 2 !!!')
            return redirect("add_partner")
    else:
        form = CustomerRegistrationForm1()
        context={
            'form':form,
                    }
        return render(request, 'AdminModule/user_registration.html',context)

def partner_add_more(request):
    user = User.objects.latest('id')
    id=user.id
    partner=ServicePartner.objects.get(user_id=id)
    if request.method == "POST":
        form = ServicePartnerRegistraionForm(request.POST,instance=partner)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For {username}')
            return redirect('view_partner')
        else:
            messages.error(request, f'Some Thing Went wrong in 2 !!!')
            return redirect("partner_add_more")
    else:
        form = ServicePartnerRegistraionForm(instance=partner)
        context={
            'form':form,
                    }
        return render(request, 'AdminModule/partner_add_more.html',context)
def view_partner(request):
    partner=ServicePartner.objects.exclude(partner_validity=None)
    return render(request,'AdminModule/view_partner.html',{'partner':partner})
def delete_partner(request,id):
    partner=ServicePartner.objects.get(id=id)
    if request.method=='POST':
        partner.delete()
        return redirect('view_area')
    else:

        context={
                'partner':partner
                   }
        return render(request, 'AdminModule/delete_partner.html', context)

def validity_extension(request,id):
    partner=ServicePartner.objects.get(id=id)
    if request.method=='POST':
        form = ValidityExtensionForm(request.POST,instance=partner)
        if form.is_valid():
            form.save()
            return redirect('view_partner')
        else:
            return render(request,'AdminModule/validity_extension.html',{'form':form})
    else:
        form=ValidityExtensionForm(instance=partner)
        return render(request,'AdminModule/validity_extension.html',{'form':form})

def view_received_bookings(request):
    bookings=Bookings.objects.filter(booking_status='Receive')
    return render(request,'AdminModule/received_bookings.html',{'bookings':bookings})

def view_confirmed_bookings(request):
    bookings=Bookings.objects.filter(booking_status='Confirm')
    return render(request,'AdminModule/confirmed_bookings.html',{'bookings':bookings})

def view_completed_bookings(request):
    bookings=Bookings.objects.filter(booking_status='Complete')
    return render(request,'AdminModule/completed_bookings.html',{'bookings':bookings})

def reviews(request):
    reviews=Feedback.objects.all()
    return render(request,'AdminModule/reviews.html',{'reviews':reviews})
