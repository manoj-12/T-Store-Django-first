from django.shortcuts import render ,redirect
from django.contrib.auth.hashers import make_password , check_password
from django.http import HttpResponse
from .models.product import Product
from .models.category import Cotegory
from .models.customer import Customer
# Create your views here.

def index(request):
    category = Cotegory.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        prod = Product.objects.filter(category=categoryID).order_by('-id')
    else:
        prod = Product.objects.all()
    print(categoryID)
    return render(request,'index.html' , {'prod':prod , 'category':category})


def signup(request):

    # print(request.method)
    if(request.method=="GET"):
        return render(request,'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        Email = postData.get('email')
        phone_number = postData.get('phonenumber')
        password = postData.get('password')
        isExist = Customer.objects.filter(email=Email)
        if isExist:
            error_massage = "User All Ready Exist"
            return render(request , "signup.html" , {"errormassage":error_massage})
        else:
            customer = Customer(first_name=first_name,
                                last_name=last_name,
                                email=Email,
                                phone=phone_number,
                                password=password)

            # password hash
            customer.password = make_password(customer.password)
            customer.save()
        return render(request,'login.html')



def log_In(request):
    if request.method =="GET":
        return render(request, "login.html")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_massage = None
        if customer:
            flag = check_password(password,customer.password)
            if flag:
                return redirect('/')
            else:
                error_massage = 'email or  password invalid'
        else:
            # error massage
            error_massage = 'email or  password invalid'
        return render(request , "login.html", {"errormassage":error_massage})