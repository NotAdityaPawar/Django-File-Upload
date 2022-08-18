from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class File(models.Model):
    
    file = models.FileField(upload_to='documents/')
    date_added = (models.DateTimeField(auto_now_add=True))

