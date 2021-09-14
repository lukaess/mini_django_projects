from django.db.models.fields import EmailField
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.

def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def show_message(request):
    message = 'If you lose, dont give up. Thats the first step to success!'
    return render(request, 'index.html', {'message': message}) 

def counter(request):
    posts = [1, 3, 4, 5, 'Lukas', 'bakman']
    return render(request, 'counter.html', {'posts': posts})

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if check_paswords(password, password2):
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Username already used')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('registration')
    return render(request, 'registration.html')

def check_paswords (password, password2):
    if password == password2:
        return True
    return False

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})

