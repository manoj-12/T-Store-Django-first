from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Cotegory


def index(request):
    if request.method == "GET":
        cart = request.session.get('cart')
        if not cart:
            request.session["cart"] = {}
        category = Cotegory.objects.all()
        categoryID = request.GET.get('category')
        if categoryID:
            prod = Product.objects.filter(category=categoryID).order_by('-id')
        else:
            prod = Product.objects.all()

        # print(categoryID)
        return render(request, 'index.html', {'prod': prod, 'category': category})

    else:
        product = request.POST.get('product_id')
        remove_cart = request.POST.get('remove_cart')
        print('Product Id ==:', product)
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove_cart:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product]=1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print("cart is  = ",cart)
    return redirect('/')
