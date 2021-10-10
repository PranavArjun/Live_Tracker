from django.db import models


# Create your models here.


class TrackerScanner(models.Model):
    ID = models.IntegerField()
    package_id= models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    gps_no_field = models.AutoField(db_column='GPS no.',  primary_key = True,
                  serialize = False, 
                  verbose_name ='ID')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    date = models.DateField(db_column='Date', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    
    
    class Meta:
        
        db_table = 'tracker_scanner'
        #unique_together = ['package_id', 'city']
       

    
        