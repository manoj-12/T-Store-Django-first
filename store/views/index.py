from django.shortcuts import render
from store .models.product import Product
from store .models.category import Cotegory


def index(request):
    category = Cotegory.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        prod = Product.objects.filter(category=categoryID).order_by('-id')
    else:
        prod = Product.objects.all()
    print(categoryID)
    return render(request, 'index.html', {'prod': prod, 'category': category})

