from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages 
from .models import Product

# Create your views here.
value = {}

def tempSave(val):
    global value 
    value = val
    return  

def getVal():
    return value
    
def dashboard(request):
    if request.method == "POST":
        user = request.user

        # Now you can access user details such as username, email, etc.
        phone = user.username
        first_name = user.first_name
        
        seller_name = first_name
        seller_phone = phone
        
        product_name = request.POST.get("pname")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        image = request.FILES["pimage"]
        
        product = Product(seller_name=seller_name, seller_phone=seller_phone, product_name=product_name, price=price, desc=desc, image=image)
        
        product.save()
        messages.success(request, " Your account has been successfully created")
        
        
        products = Product.objects.filter(seller_phone=seller_phone, seller_name=first_name).values()
        print(products)
        n = len(products)
        params = {'range': range(0,n),'product': products}
        tempSave(params)
        # print(params)
        # return render(request, 'shop/home.html', params)
        return render(request, 'dashboard/sellerdashboard.html', params)
    
    else:
        user = request.user

        # Now you can access user details such as username, email, etc.
        seller_phone = user.username
        first_name = user.first_name
        
        print(seller_phone)
        
        
        products = Product.objects.filter(seller_phone=seller_phone, seller_name=first_name).values()
        n = len(products)
        params = {'range': range(0,n),'product': products}
        tempSave(params)
        
        return render(request, 'dashboard/sellerdashboard.html', params)

def product(request):
    user = request.user

    # Now you can access user details such as username, email, etc.
    seller_phone = user.username
    first_name = user.first_name
    
    print(seller_phone)
    
    
    products = Product.objects.filter(seller_phone=seller_phone).values()
    n = len(products)
    params = {'range': range(0,n),'product': products}
    tempSave(params)
    
    return render(request, 'dashboard/productList.html', params)
    
    
def delete(request, id):
    dlt = Product.objects.get(id=id)
    dlt.delete();
    
    return redirect("/dashboard")
