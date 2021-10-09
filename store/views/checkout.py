from django.shortcuts import render, redirect
from store .models .product import Product
from store .models .orders import Order
from store .models .customer import Customer

def checkout(request):
    if request.method == 'POST':
        phone = request.POST.get('phone_number')
        address = request.POST.get('address')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        product = Product.objects.filter(id__in=cart.keys())
        for product in product:
            orderSave = Order(Phone=phone ,
                              Address=address ,
                              customer=Customer(id=customer),
                              Quantity=cart.get(str(product.id)),
                              product=product,
                              Price = product.Price
                          )
        orderSave.save()
        request.session["cart"]={}
        # print(phone , address , customer , cart , product)
        return redirect('/cart')


