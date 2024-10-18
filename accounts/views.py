from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UserForm
from vendor.forms import VendorForm
from .models import User,UserProfile
from django.contrib import messages
from django.urls import reverse
from django.contrib import auth
from .utils import detectUser,send_verification_email
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.exceptions import PermissionDenied
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# in a django in a user regestration form there is a two types of error is occured 
# validation error(it occur when something wrong happend with a model) ,

#  non field errors it are not assosication with a non filed errors a 
# restriciting the vendor for accessing the customer page
def check_role_vendor(user):   # it is use for a security purpose when vendor want to access a costumer id directly 
    if user.role==1:         # then it cant we reach
        return True
    else:
        return PermissionDenied
def check_role_costumer(user):
    if user.role==2:
        return True
    else:
        return PermissionDenied 
#Then, apply this decorator to the function where you are encountering the error to check if the issue is resolved:

@csrf_exempt       
def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request,"you are already logged in !")
        return redirect('dashboard')
    if request.method=='POST':
        print(request.POST)
        form=UserForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data['password']
            user=form.save(commit=False)
            user.set_password(password)
            user.role=User.CUSTOMER
            user.save()
            #send_verification_email(request,user)
            
            #it is used to send a verification email it function mainly presnet in utils.py

            # Define mail_subject and email_template
            mail_subject = "Verify Your Account"
            email_template = "accounts/emails/account_verification_email.html"

            
            send_verification_email(request,user,mail_subject,email_template)
            messages.success(request,'User created successfully')
            return redirect('registerUser')
        else:
            print('invalid form')
            print(form.errors)    # it is used to give a field error 
    else:
        form=UserForm()
    context={
        'form':form,
    }
    
    return render(request, 'accounts/registerUser.html', context)
@csrf_exempt  
def registerVendor(request):
    if request.user.is_authenticated:
        messages.warning(request,"you are already logged in !")
        return redirect('dashboard')
    if request.method == 'POST':
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.VENDOR
            user.save()

            vendor = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)  # Ensure correct model
            vendor.user_profile = user_profile
            vendor.save()
            # after saving a verification it can help to send a verification to email fo comfirmation
            send_verification_email(request,user)
            messages.success(request, 'Your account has been registered successfully')
            return redirect(reverse('registerVendor'))
        else:
            print('Invalid form')
            print(form.errors)  # Field errors
            messages.error(request, 'There was an error with your submission.')
    else:
        form = UserForm()
        v_form = VendorForm()
    
    context = {
        'form': form,
        'v_form':v_form,
    }
    return render(request, 'accounts/registervendor.html', context)
def activate(request, uidb64, token):
    # Activate the user by setting the is_active status to True
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulation! Your account is activated.')
        return redirect('myAccount')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('myAccount')

def login(request):
    if request.user.is_authenticated:
        messages.warning(request,"you are already logged in !")
        return redirect('myAccount')
    elif request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"you are login ")
            return redirect("myAccount")
        else:
            messages.error(request,"inavlid try")
            return redirect('login')     # redirect uss function kay call karega jisnka naam tumne dia hai 


    return render(request,'accounts/login.html')
def logout(request):
    auth.logout(request)
    messages.info(request,'you are logged out')
    return redirect("login")
    #return  render(request,'accounts/logout.html')
    # 
    # 
@login_required(login_url='login') 
def myAccount(request):
    user=request.user
    redirectUrl=detectUser(user)
    return redirect(redirectUrl)
@login_required(login_url='login')
@user_passes_test(check_role_costumer)
def custDashboard(request):
    return render(request, 'accounts/custDashboard.html')
@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vendorDashboard(request):
    return render(request,'accounts/vendorDashboard.html')