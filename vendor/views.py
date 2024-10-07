from django.shortcuts import render,redirect
from accounts.forms import UserForm,User
from .forms import VendorForm
from accounts.models import UserProfile
from django.contrib import messages
# Create your views here.
def registerVendor(request):
    if request.method=='POST':
        #store the data and create the user 
        form =UserForm(request.POST)
        v_form=VendorForm(request.POST,request.FILES)

        if form.is_valid() and v_form.is_valid():
             
          first_name=form.cleaned_data['first_name']
          last_name=form.cleaned_data['last_name']
          username=form.cleaned_data['username']
          email=form.cleaned_data['email']
          password=form.cleaned_data['password']
          user =User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
          user.role=User.RESTAURANT 
          user.save()

          vendor=v_form.save(commit=False)
          vendor.user=user 
          user_profile=UserProfile.objects.get(user=user)
          vendor.user_profile=user_profile
          vendor.save()
          messages.success(request,'your account will be registered soon')
          return redirect('myapp:index')
        else:
             context={
               'form':form,
               'v_form':v_form
                      }
             return render(request,'vendor/registerVendor.html',context)

    else:

        form=UserForm()
        v_form=VendorForm()
        context={
        'form':form,
        'v_form':v_form
        }
    return render(request,'vendor/registerVendor.html',context)

    
