from django.conf import settings
from django.db import models

# Create your models here.


class CompanyDb(models.Model):
    Project_Name = models.CharField(max_length=50, unique=True)
    Brand_Name = models.CharField(max_length=50,)
    Address = models.CharField(max_length=255, blank=True, null=True,)
    Phone_Number = models.CharField(max_length=10, blank=True, null=True,)
    Email = models.EmailField(max_length=50, blank=True, null=True)
    Created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    Type = models.CharField(max_length=50, default='Company Theme')

    def __str__(self):
        return self.Project_Name


class DataDb(models.Model):
    text = models.CharField(max_length=200, blank=True)
    date = models.DateField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True)
    Project_Name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.text
