from django.db import models
from django.db.models.fields import DateField


# Create your models here.


class TrackerScanner(models.Model):
    package_id= models.IntegerField(unique=True)
    Date = models.DateField(default="2021-12-12")
    gps_no_field = models.URLField(default="https://www.google.com/maps/@18.1611145,74.5895199,14z")
   
    
    class Meta:
        
        db_table = 'tracker_scanner'
        #unique_together = ['package_id', 'city']
       

    
        