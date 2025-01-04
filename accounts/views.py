from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == "POST":
        messages.error(request, 'Testing error messaging')
        return redirect('signin')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        # Validation
        # Check if passwords match
        if password == password2:
            return
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
        
    else:
        return render(request, 'accounts/register.html')

def logout():
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/register.html')
