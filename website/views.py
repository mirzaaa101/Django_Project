from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Records

def home(request):
    records = Records.objects.all()
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

    return render(request, 'website/home.html', {'records':records})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.error(request, "You have been logged out!!")
    return redirect('views.home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.error(request, "You Have Successfully Registered! Welcome!")
			return redirect('views.home')
	else:
		form = SignUpForm()
		return render(request, 'website/register_user.html', {'form':form})

	return render(request, 'website/register_user.html', {'form':form})


def customer_records(request, pk):
      if request.user.is_authenticated:
            # look up records
            customer_record = Records.objects.get(id=pk)
            return render(request, 'website/records.html', {'customer_record':customer_record})
      else:
            messages.error(request, "You must login to see customer details!!")
            return redirect('views.home')
