
# Create your views here.

import stripe
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_payment_intent(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        currency = 'usd'

        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=int(amount),
            currency=currency,
            payment_method_types=["card"],
        )

        payment = Payment.objects.create(
            amount=amount,
            currency=currency,
            payment_intent_id=intent['id'],
            status='created',
        )

        return JsonResponse({
            'client_secret': intent['client_secret'],
            'payment_intent_id': intent['id'],
        })

    return render(request, 'payments/create_payment.html')

def payment_success(request):
    return render(request, 'payments/payment_success.html')