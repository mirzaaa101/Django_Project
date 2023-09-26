from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Check if user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.error(request, "You have been logged in!")
            return redirect('views.home')
        else:
            messages.error(request, 'Username/Password is incorrect, please try again!')
            return redirect('views.home')

    return render(request, 'website/home.html', {})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.error(request, "You have been logged out!!")
    return redirect('views.home')

def register_user(request):
   return render(request, 'website/register_user.html', {})