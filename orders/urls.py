  
from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('cash_payment/<int:order_id>/', views.cash_payment, name='cash_payment'),
    path('order_complete/', views.order_complete, name='order_complete'),
]