from django.db import models

# Create your models here.
class Academic(models.Model):
    title = models.CharField(max_length = 200)
    authors = models.TextField()
    
    link = models.TextField() 
    
