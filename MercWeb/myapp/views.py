from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def inventory(request):
    return render(request, 'inventory.html')

def car_details(request):
    return render(request, 'car_details.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def checkout(request):
    return render(request, 'checkout.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')

def profile(request):
    return render(request, 'profile.html')

def testimonials(request):
    return render(request, 'testimonials.html')