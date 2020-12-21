from django.shortcuts import render, redirect
from register.forms import RegisterForm
from store.models import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            customer = Customer()
            Customer.user = User
            Customer.name = User.username
            Customer.email = User.email
            customer.save()
        return redirect("/login/")
    else:
        form = RegisterForm()

    form = RegisterForm()
    return render(response, 'register/register.html', {'form': form})


def logout(request):
    return redirect('/')

