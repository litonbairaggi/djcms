from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    # count total Customer
    total_customers = customers.count()

    # count total Order
    total_orders = orders.count()
    # count total delivered Order  
    delivered = orders.filter(status='Delivered').count()
    # count total pending Order 
    pending = orders.filter(status='Pending').count()

    # 'orders' ---> it's going on  .html page 
    context = {
        'orders': orders, 
        'customers': customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'accounts/products.html', context)

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count
    }

    return render(request, 'accounts/customer.html', context)
