from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='Dashboard'),
    path('product/', views.product, name='Product'),
    path('delete/<int:id>', views.delete, name='Delete'),
]