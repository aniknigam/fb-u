from django.db import models

# Create your models here.
class Register(models.Model):
    sellername = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10, default="")
    password = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=50, default="")
    additionaldetail = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.sellername