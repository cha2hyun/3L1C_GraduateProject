from django.conf import settings
from django.db import models

# Create your models here.


class DataDb(models.Model):
    title = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='product', blank=True)
    location = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=200, blank=True)
    howtotrade = models.CharField(max_length=200, blank=True)
    review = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True)
    Project_Name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title
