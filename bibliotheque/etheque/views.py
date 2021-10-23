from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm, RegistrationForm
# Create your views here.

class home(View):
    def get(self, request):
        forms = Livre.objects.all()
        return render(request, "home.html", {'forms':forms})

class detail(View):
    def get(self, request, idp):
        livre = Livre.objects.get(id = idp)
        return render(request, "detail.html", {'livre':livre})

def cart_add(request, livre_id):
    cart = request.session.get(settings.CART_SESSION_ID, {})
    livre = Livre.objects.get(id = livre_id)
    if livre_id not in cart:
        cart[livre_id] = {'quantity': 1, 'titre':livre.titre}

    request.session[settings.CART_SESSION_ID] = cart
    return redirect('home')

def cart_detail(request):
    cart = request.session.get(settings.CART_SESSION_ID, {})

    for key, val in cart.items():
        livre = Livre.objects.get(id = key)
        cart[str(livre.id)]['livre'] = livre

    return render(request, "cart_detail.html", {'cart':cart})

def cart_remove(request, livre_id):
    cart = request.session.get(settings.CART_SESSION_ID)
    if str(livre_id) in cart:
        del cart[str(livre_id)]

    request.session[settings.CART_SESSION_ID] = cart
    return redirect('cart_detail')

def signin(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context = {
        'form': forms
    }
    return render(request, 'signin.html', context)

def signup(request):
    forms = RegistrationForm()
    if request.method == 'POST':
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            firstname = forms.cleaned_data['firstname']
            lastname = forms.cleaned_data['lastname']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            confirm_password = forms.cleaned_data['confirm_password']
            if password == confirm_password:
                try:
                    User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                    return redirect('signin')
                except:
                    context = {
                        'form': forms,
                        'error': 'This Username Already exists!'
                    }
                    return render(request, 'signup.html', context)
    context = {
        'form': forms
    }
    return render(request, 'signup.html', context)

def profil(request):
    if request.user.is_authenticated:
        user = User.objects.get(id = request.user.id)
    
    return render(request, "profil.html", {'user':user})

def signout(request):
    logout(request)
    return redirect('signin')

def rechercher(request):
    forms = Livre.objects.filter(titre__icontains = request.POST.get("cle"))
    return render(request, "home.html", {'forms':forms})

def emprunt(request):
    cart = request.session.get(settings.CART_SESSION_ID)

    for key, val in cart.items():
        livre = Livre.objects.get(id = int(key))
        user = User.objects.get(id = request.user.id)
        Emprunt.objects.create(livre = livre, client = user)
    
    del request.session[settings.CART_SESSION_ID]
    return render(request, "emprunter.html", {})

def Emprunts(request):
    if request.user.is_authenticated:
        livres = Livre.objects.raw('SELECT * from etheque_livre, auth_user, etheque_emprunt WHERE etheque_livre.id = etheque_emprunt.livre_id and auth_user.id = etheque_emprunt.client_id')
    
    return render(request, "emprunts.html", {'livres':livres})
    

