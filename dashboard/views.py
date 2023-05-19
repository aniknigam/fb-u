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
        product_name = request.POST.get("pname")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        seller_name = request.POST.get("sellername")
        seller_phone = request.POST.get("sellerphone")
        image = request.FILES["pimage"]
        
        product = Product(seller_name=seller_name, seller_phone=seller_phone, product_name=product_name, price=price, desc=desc, image=image)
        
        product.save()
        messages.success(request, " Your account has been successfully created")
        
        
        products = Product.objects.filter(seller_phone=seller_phone).values()
        n = len(products)
        params = {'range': range(0,n),'product': products}
        tempSave(params)
        # print(params)
        # return render(request, 'shop/home.html', params)
        return render(request, 'dashboard/sellerdashboard.html', params)
    
    else:
        # current_user = request.user
        # # print(current_user.first_name)
        # products = Product.objects.filter(seller_name=current_user.first_name).values()
        # n = len(products)
        # params = {'range': range(0,n),'product': products}
        return render(request, 'dashboard/sellerdashboard.html')

def product(request):
    if request.method == "POST":
        seller_phone = request.POST.get("sellerphone")        
        
        products = Product.objects.filter(seller_phone=seller_phone).values()
        n = len(products)
        params = {'range': range(0,n),'product': products}
        tempSave(params)
        # print(params)
        # return render(request, 'shop/home.html', params)
        return render(request, 'dashboard/productList.html', params)
    
    else:
        return render(request, 'dashboard/productList.html')
    
def delete(request, id):
    dlt = Product.objects.get(id=id)
    dlt.delete();
    
    return redirect("/dashboard/product/")
