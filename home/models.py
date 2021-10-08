from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self) :
        return 'Message from ' + self.name + ' -->' + self.email
        



class Order(models.Model):
    Orderid = models.IntegerField()
    OrderDate = models.DateField()
    GPs_link = models.URLField() 
 
    def __str__(self):
        return str(self.Orderid)