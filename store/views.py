from django.shortcuts import redirect, render
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

# Create your views here.
def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {"product": product})

def home(request): 
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})

def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in!"))
            return redirect('home')
        else:
            messages.success(request, ("An error occured."))
            return redirect('login')
    else:
        return render(request, "login.html", {})

def logoutUser(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('home')

def registerUser(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            # log in users
            user = authenticate(username = username, password = password)
            messages.success(request, ("You have registered successfully!"))           
            login(request, user)
            return redirect("home")
        else:
            messages.success(request, ("There was a problem")) 
            return redirect("register")          

    else: 
        return render(request, "register.html", {"form": form})