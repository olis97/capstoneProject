from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth.models import User

# Function renders user login view
def user_login(request):
    if request.user.is_authenticated:
        current_user = request.user
        return HttpResponseRedirect(reverse('users:profile'))
    else:
        current_user = None
        return render(request, 'user_login.html')

# Function implements signup logic and renders view
def user_signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

       # Create a New User & Save to Database
        try:             
            user = User.objects.create_user(username=email, password=password)
            user.first_name = firstname
            user.last_name = lastname                                            
            user.is_staff = False
            user.is_superuser = False
            # Save user to Db
            user.save()
            login(request, user)
            # Redirect user
            return HttpResponseRedirect(reverse('users:profile'))            
        except:                        
            # Redirect user
            return render(request, 'user_create.html')
    else:
        return render(request, 'user_create.html')
        

# Function renders user profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'user_profile.html', {   
            "firstname": request.user.first_name,
            "lastname": request.user.last_name,
            "email": request.user.username, })
    else:
        return HttpResponseRedirect(reverse('users:login'))

# Function implements user authentication
def user_authentication(request):
    email = request.POST['email']
    password = request.POST['password']    
    # Authorize user
    user = authenticate(username=email, password=password)
    # User is NOT Authenticated
    if user is None:
        # Update result parameter to pass to view
        error_message = "Invalid Username or Password!"
        # Construct reverse URL for Http Response Redirect
        return render(request, 'user_login.html', {'error_message': error_message})
    else:
        # Login user 
        login(request, user)
        return HttpResponseRedirect(reverse('users:profile'))

# Function implements user logout functionality
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

def user_delete(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
