
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('remove-food/', views.remove_food, name='remove_food'),
    path('contact/', views.contact, name='contact'),
    path('calculator/', views.calculator, name='calculator'),
   
]
