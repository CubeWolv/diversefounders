from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login



 
@login_required
def dashboard(request):
    firstname = request.user.first_name
    lastname = request.user.last_name
    email=request.user.email
    return render(request, "dashboard.html",{'firstname': firstname,'lastname':lastname, 'email':email})


def login(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        

        user = authenticate(request, username=username, password=password)

        if user is not None:
            dj_login(request, user)
            return redirect('dashboard')

        else:
            messages.info(request, 'Invalid username or password')
            return redirect("login")

    return render(request, 'forms/login.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('login')


def signup(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard.html')

    context = {'form': form}
    return render(request, 'forms/signup.html', context)