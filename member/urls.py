from django.urls import path, include
from . import views

urlpatterns = [
    path('sellerLogin/', views.index, name='SellerLogin'),
    # path('adminLogin/', views.adminLogin, name='AdminLogin'),
    # path('admindashboard/', views.adminDashboard, name='AdminDashboard'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('register/', views.register, name='SellerRegister'),
]