from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.orders import Order


def order(request):
    customer = request.session.get('customer')
    order = Order.objects.filter(customer=customer).order_by("-Date")
    print(customer, order)
    return render(request, "order.html", {"orders": order})
