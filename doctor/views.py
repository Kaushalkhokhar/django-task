from django.contrib import auth
from django.shortcuts import render, redirect, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import DoctortCreationForm, DoctorLoginForm
from .models import Doctor
from hashlib import sha1


def login(request):
    if request.method == 'POST':
        form = DoctorLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            doctor = authenticate(email=email, password=password)
            if doctor:
                login(request, doctor)
                return redirect('list') 
            messages.error(request, f'Please enter valid email and password')        
    else:
        form = DoctorLoginForm()
    return render(request, 'doctor/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = DoctortCreationForm(request.POST)
        if form.is_valid():
            form.save() # to save a form data
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!. You are now able to login')
            return redirect('login')

    else:
        form = DoctortCreationForm()
    return render(request, 'doctor/register.html', {'form': form})

@login_required
def list(request):
    print(request.user)
    return render(request, 'doctor/register.html')