from django.db import models

# Create your models here.

class TrackerScanner(models.Model):
    id = models.BigAutoField(primary_key=True)
    package_id = models.IntegerField(unique=True)
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    gps_no_field = models.URLField(default="https://www.google.com/maps/place/Mumbai")

    class Meta:
        managed = False
        db_table = 'tracker_scanner'