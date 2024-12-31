from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, LoginForm
from .models import Farmer
import logging

logger = logging.getLogger(__name__)

def home(request):
    if request.user.is_authenticated:
        return redirect('users:dashboard')
    return render(request, 'users/home.html', {
        'title': 'Home'
    })

def register(request):
    if request.user.is_authenticated:
        return redirect('users:dashboard')
        
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('users:dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('users:dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back {username}!')
                return redirect('users:dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('users:login')

@user_passes_test(lambda u: u.is_superuser)
def user_list(request):
    farmers = Farmer.objects.filter(user_type='farmer')
    buyers = Farmer.objects.filter(user_type='buyer')
    
    context = {
        'farmers': farmers,
        'buyers': buyers,
    }
    return render(request, 'users/user_list.html', context)

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html', {
        'title': 'Dashboard'
    }) 