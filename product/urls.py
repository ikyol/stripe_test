from django.urls import path
from .views import item_view, get_stripe_session, CancelView, SuccessView

urlpatterns = [
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('item/<int:id>/', item_view, name='item'),
    path('buy/<int:id>/', get_stripe_session, name='buy'),
]