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
        


class TrackerScanner(models.Model):
    id = models.BigAutoField(primary_key=True)
    package_id = models.IntegerField(unique=True)
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    gps_no_field = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tracker_scanner'