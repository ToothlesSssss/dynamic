# file: appName/models.py

from django.db import models

# Create your models here.

# company info 
# products 
class Author(models.Model):
   author  = models.CharField(max_length=100)
   

   def __str__(self) -> str:
      return self.author

class Book(models.Model):
   book = models.CharField(max_length=100)
   product_description = models.TextField()   
   Author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
   image  = models.ImageField(null=True)
   price   = models.CharField(max_length=100, null=True)
   date   = models.DateTimeField(auto_now_add=True, null=True)
   
   def __str__(self) -> str:
      return self.book
   

class Custom(models.Model):
   name = models.CharField(max_length=100,null=True)
   email  = models.EmailField(null=True)
   phone =models.FloatField()
   text  = models.TextField()

   def __str__(self) -> str:
     return self.name
   
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name
