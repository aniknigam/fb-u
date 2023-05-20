"""
URL configuration for FabricBecho project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='AdminDashboard'),
    path('', views.index, name='Home'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    path('search/', views.search, name='Search'), 
    path('allproducts/', views.allproducts, name='AllProducts'),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path('privacyPolicy/', views.privacyPolicy, name='PrivacyPolicy'),
    path('termsAndConditions/', views.termsAndConditions, name='TermsAndConditions'),
    path('returnPolicy/', views.returnPolicy, name='ReturnPolicy'),
    path('member/', include('member.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('requirements/', include('postrequirement.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configure Admin Titles
admin.site.site_header = "FabricBecho Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to FabricBecho Admin Portal"