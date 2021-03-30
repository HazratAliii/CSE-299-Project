from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import tourist_DB
from .models import Guides, Hotels, Tourists
# Create your views here.
def tregister(request):
    # if request.method == 'POST':
    #     form = tourist_DB(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data('name')
    #         messages.success(request, f'Account created for {username}')
    #         return redirect('app1-home')
    # else:
    #     form = tourist_DB()
    #     return render(request, 'user/register.html', {'form': form})
    return render(request, 'user/register.html')

def register_sub(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']
    password2 = request.POST['password2']
    guides = Guides(name = name, email = email, phone = phone, password = password, password2 = password2)
    guides.save()
    return render(request, 'app1/home.html', {})

def profile(request):
    return render(request, "user/profile.html", {})

def login(request):
    return render(request, 'user/login.html', {})

def login_sub(request):
    if request.Method == "POST":
        return render(request, "user/home.html", {})
    else:
        return render(request, 'user/profile.html', {})

def hotels(request):
    return render(request, 'user/hotels.html')

def hotel_info_sub(request):

    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    description = request.POST['description']
    available = request.POST['available']
    # print(name)
    # print(email)
    # print(phone)
    # print(description)
    # print(available)
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
    return render(request, 'user/touristSign.html')

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
    return render(request, 'app1/home.html', {})

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

def rangamati_sub(request):
    data = Hotels.objects.all()
    return render(request, 'user/hotelP.html', {'info' : data})

def rangamati_sub(request):
    data = Hotels.objects.all()
    return render(request, 'user/hotelP.html', {'info' : data})

def sundarban_sub(request):
    data = Hotels.objects.all()
    return render(request, 'user/hotelP.html', {'info' : data})

def kuakata_sub(request):
    data = Hotels.objects.all()
    return render(request, 'user/hotelP.html', {'info' : data})

def coxsbazar_sub(request):
    data = Hotels.objects.all()
    return render(request, 'user/hotelP.html', {'info' : data})