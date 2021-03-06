from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password

from store .models.customer import Customer

def log_In(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        print(customer)
        error_massage = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                # request.session['email'] = customer.email
                return redirect('/')
            else:
                error_massage = 'email or  password invalid'
        else:
            # error massage
            error_massage = 'email or  password invalid'
        return render(request, "login.html", {"errormassage": error_massage})


def logout(request):
    request.session.clear()
    return redirect('login')