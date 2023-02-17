from django.shortcuts import render, get_object_or_404
from .models import Item
import stripe
from django.http import JsonResponse
from django.conf import settings
from django.views.generic import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY

class SuccessView(TemplateView):
    template_name = 'success.html'

class CancelView(TemplateView):
    template_name = 'cancel.html'

def get_stripe_session(request, id):
    item = Item.objects.get(id=id)
    DOMAIN = 'http://0.0.0.0:8000'
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(item.price * 100),
                    'product_data': {
                        'name': item.name,
                        'description': item.description
                    }
                },
                'quantity': 1
            }
        ],
        mode='payment',
        success_url=DOMAIN + '/success/',
        cancel_url=DOMAIN + '/cancel/',
    )
    return JsonResponse({'session_id': session.id})

def item_view(request, id):
    item = get_object_or_404(Item, id=id)
    context = {
        'item': item,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'index.html', context)


