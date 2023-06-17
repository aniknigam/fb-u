from django.db import models

# Create your models here.
class FeaturedSeller(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='featuredSeller/images')