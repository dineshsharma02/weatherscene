from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model):
    # user = models.ForeignKey(To=User,on_delete=models.CASCADE,null=True,blank=True)
    
    name = models.CharField(max_length=50)
    # state = models.CharField(max_length=50)
    # temprature = models.DecimalField(max_digits=4,decimal_places=1)
    # humidity = models.DecimalField(max_digits =4,decimal_places=1)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Cities'

