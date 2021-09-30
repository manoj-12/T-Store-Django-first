from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from store .models.customer import Customer



def signup(request):
    # print(request.method)
    if (request.method == "GET"):
        return render(request, 'signup.html')
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
            return render(request, "signup.html", {"errormassage": error_massage})
        else:
            customer = Customer(first_name=first_name,
                                last_name=last_name,
                                email=Email,
                                phone=phone_number,
                                password=password)

            # password hash
            customer.password = make_password(customer.password)
            customer.save()
        return render(request, 'login.html')
