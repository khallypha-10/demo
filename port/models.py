from django.db import models

# Create your models here.

class Featured(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='media')
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    subject =models.CharField(max_length=150)
    name = models.CharField( max_length=150)
    email = models.EmailField(max_length=254, blank=False)
    message = models.TextField()
    sent = models.DateTimeField(auto_now_add=True, null=True)