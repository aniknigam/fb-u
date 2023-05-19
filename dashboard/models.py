from django.db import models
from datetime import date

# Create your models here.
class Product(models.Model):
    
    choices = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    seller_name = models.CharField(max_length=50, default="")
    seller_phone = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="shop/images", default="")
    featured_product = models.CharField(max_length=3, choices=choices, default="No", blank=True)
    
    def __str__(self):
        return self.product_name