from django.db import models
from django.db.models.fields import DateField

# Create your models here.

class TrackerScanner(models.Model):
    id = models.BigAutoField(primary_key=True)
    package_id = models.IntegerField(unique=True)
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    gps_no_field = models.URLField(default="https://www.google.com/maps/@18.1595855,74.5812828,14z")

    class Meta:
        managed = False
        db_table = 'tracker_scanner'