from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=150)
  desc = models.TextField()

class Contact(models.Model):
  username=models.CharField( max_length=100)
  email=models.EmailField(max_length=254)
  phone=models.CharField(max_length=10)
  text=models.CharField( max_length=254)

#for simplicity
  def __str__(self):
      return self.email
  

