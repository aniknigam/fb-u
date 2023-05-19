from django.db import models
from datetime import date

# Create your models here.
class Requirement(models.Model):
    requirement_id = models.AutoField
    requirement_text = models.CharField(max_length=300)
    pub_date = models.DateField(default=date.today)