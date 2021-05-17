from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import tourist_DB
from .models import Guides, Hotels, Tourists
# Create your views here.
def tregister(request):
    email = request.POST['email']
    password = request.POST['password']

    if Tourists.objects.filter(email = email, password = password):
        return render(request, "app1/home.html", {})
    else:
        return render (request, "user/login.html")

def register_sub(request):

    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']
    password2 = request.POST['password2']
    guide = Guides(name = name, email = email, phone = phone, password = password, password2 = password2)
    guide.save()
    return render(request, 'app1/home.html', {})

def profile(request):
    guides = Guides.objects.all()
    return render(request, "user/profile.html", {"guide": guides})

def login(request):
    data = Guides.objects.all()
    return render(request, 'user/login.html', {'data': data})

def login_sub(request):
    email = request.POST['email']
    password = request.POST['password']

    guide = Guides.objects.filter(email = email, password = password)
    if guide:
        return render(request, "user/profile.html", {'guide': guide})
    else:
        return render (request, "user/login.html")

def hotels(request):
    return render(request, 'user/hotels.html')

def hotel_info_sub(request):

    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    description = request.POST['description']
    available = request.POST['available']
    hotels = Hotels(name = name, email = email, phone = phone, description = description, available = available)
    hotels.save()
    return render(request, 'app1/home.html')

def hotel_page(request):
    # data = Hotels.objects.get(name = 'Hotel 1')
    return render(request, 'user/hotelP.html', )
    
def about_us(request):
    data = Hotels.objects.get(big_city_name = 'Rangamati')
    return render(request, 'user/about_us.html', {'info' : data})

def hotel_list(request):
    hotels = Hotels.objects.all()
    return render(request, 'user/hotel_list.html', {'hotel' : hotels})

def tourist_login(request):
    return render(request, 'user/touristLogin.html')

def guide_login(request):
    return render(request, 'user/guideLogin.html')

def guide_signup(request):
    return render(request, 'user/guideSign.html')

def tourist_signup(request):
    return render(request, 'user/touristSign.html')

def tourist_register_sub(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']
    password2 = request.POST['password2']
    tourist = Tourists(name = name, email = email, phone = phone, password = password, password2 = password2)
    tourist.save()
    return render(request, 'user/touristLogin.html', {})

def rangamati(request):
    data = Hotels.objects.all()
    return render(request, 'user/rangamati.html', {'hotel' : data})

def sundarban(request):
    data = Hotels.objects.all()
    return render(request, 'user/Sundarban.html', {'hotel' : data})

def coxsbazar(request):
    data = Hotels.objects.all()
    return render(request, "user/coxsbazar.html", {'hotel' : data})

def kuakata(request):
    data = Hotels.objects.all()
    return render(request, 'user/Kuakata.html', {'hotel' : data})

def rangamati_sub(request, pk):
    data = Hotels.objects.get(id = pk)
    context = {'data': data}
    return render(request, 'user/hotelP.html', context)
   
def sundarban_sub(request, pk):
    data = Hotels.objects.get(id = pk)
    context = {'data': data}
    return render(request, 'user/hotelP.html', context)

def kuakata_sub(request, pk):
    data = Hotels.objects.get(id = pk)
    context = {'data': data}
    return render(request, 'user/hotelP.html', context)

def coxsbazar_sub(request, pk):
    data = Hotels.objects.get(id = pk)
    context = {'data': data}
    return render(request, 'user/hotelP.html', context)

def guide_info(request):
    return render(request, "user/guideinfo.html")