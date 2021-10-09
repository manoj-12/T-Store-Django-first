from django import template

register = template.Library()


@register.filter(name='Product_in_cart')
def Product_in_cart(product, cart):
    key = cart.keys()
    for id in key:
        # print(id, key)
        # print(type(id), type(product.id))
        if int(id) == product.id:
            return True
    return False;


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    key = cart.keys()
    for id in key:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name='Total_Price')
def Total_Price(product, cart):
    return product.Price * cart_quantity(product, cart)


@register.filter(name='Total_Price_Cart')
def Total_Price_Cart(product, cart):
    sum = 0;
    for prod in product:
        sum += Total_Price(prod , cart)
    return sum
