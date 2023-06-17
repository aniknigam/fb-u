from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from .models import Register

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # if request.user.is_superuser:
            #     return redirect("/admin/")
            return redirect("Dashboard")
        else:
            # messages.success(request, ("Invalid Credentials, Please try again"))
            return redirect("/login")
    else:
        return render(request, 'member/slogin.html')
    

def adminLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("AdminDashboard")
            return redirect("AdminLogin")
        else:
            messages.success(request, ("Invalid Credentials, Please try again"))
            return redirect("AdminLogin")
    else:
        return render(request, 'member/adminlogin.html')

def logoutUser(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect("Home")

def register(request):
    if request.method=="POST":
        # Get the post parameters
        sellername=request.POST['sellername']
        email=request.POST['email']
        sellerphone=request.POST['sellerphone']
        address=request.POST.get('address', '')
        password=request.POST['createpass']
        cpassword=request.POST['confpass']
        additionaldetail=request.POST['additionaldetail']

        if password!=cpassword:
            messages.success(request, " Passwords do not match")
            return redirect('register')
        
        # Create the user
        myuser = User.objects.create_user(sellerphone, email, password)
        myuser.first_name= sellername
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        
        
        reg = Register(sellername=sellername, phone=sellerphone, email=email, address=address, additionaldetail=additionaldetail)
        reg.save()
        messages.success(request, " Your account has been successfully created")
        
        return redirect('SellerLogin')

    else:
        return render(request, 'member/sellerregister.html')

def adminDashboard(request):
    return render(request, 'member/admindashboard.html')