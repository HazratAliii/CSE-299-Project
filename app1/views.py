from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app1/home.html')

def register(request):
    return render(request, 'app1/register.html')


