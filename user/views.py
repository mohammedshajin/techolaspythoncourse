from django.shortcuts import redirect, render
from .forms import techolasUserForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User


def signup(request):
    form = techolasUserForm()
    
    if request.method == 'POST':
        form = techolasUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)

            return redirect('home')
        else:
            return redirect('signup')

    context = {'form':form}

    return render(request, 'signup.html', context)

def logout(request):
    django_logout(request)
    return redirect('home')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'login.html')


