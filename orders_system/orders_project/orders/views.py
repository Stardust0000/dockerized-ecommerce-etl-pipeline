from django.shortcuts import render
from django.http import JsonResponse
from .models import Order

def get_orders(request):
    orders = list(Order.objects.values()) 
    # Order.objects.values() gives queryset 
    # list(...) converts queryset to Python list bcz JsonResponse can't serialize queryset directly
    return JsonResponse(orders, safe=False) #returns API response as JSON