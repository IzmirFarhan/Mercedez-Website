from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('inventory', views.inventory, name='inevntory'),
    path('car_details', views.car_details, name='car_details'),
    path('services', views.services, name='services'),
    path('contact',views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('checkout', views.checkout, name='checkout'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('profile', views.profile, name='profile')
]