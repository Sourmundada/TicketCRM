from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Account, Staff
from django.contrib.auth.decorators import login_required

def admin_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            return redirect('index')
        else:
            login(request, user)
            return redirect('admin_home')   

    return render(request, 'owner/admin_login.html')

@login_required(login_url='admin_login')
def admin_logout(request):
    logout(request)
    return redirect('index')

# Staff

def staff_register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            new_member = Staff.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
            new_member.save()
            login(request, new_member)
            return redirect('staff_home')
        else:
            return redirect('index')

    return render(request, 'staff/staff_register.html')

def staff_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            return redirect('index')
        else:
            login(request, user)
            return redirect('staff_home')

    return render(request, 'staff/staff_login.html')

@login_required(login_url='staff_login')
def staff_logout(request):
    logout(request)
    return redirect('index')