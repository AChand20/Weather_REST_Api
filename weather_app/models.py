from django.db import models
from django.conf import settings
#from django.utils.timezone import TIME_ZONE

# Create your models here.
class Weather(models.Model):
    location = models.CharField(max_length=10)
    metric = models.CharField(max_length=10)
    year = models.IntegerField()
    month = models.IntegerField()
    value = models.DecimalField(max_digits=10,decimal_places=1)

    class Meta:
        unique_together = (('location','metric','year','month','value'),)
