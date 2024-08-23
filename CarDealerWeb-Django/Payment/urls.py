# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('create_payment_intent/', views.create_payment_intent, name='create_payment_intent'),
     path('payment-success/', views.payment_success, name='payment_success'),
]
