from django.shortcuts import render
from store .models .product import Product
def cart(request):
    ids = request.session.get('cart').keys()
    product = Product.objects.filter(id__in=ids)
    print("cart in product = ",product)
    return render(request, "cart.html" , {"product":product})


