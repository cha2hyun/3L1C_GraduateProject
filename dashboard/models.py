from django.conf import settings
from django.db import models


# Create your models here.


class createDb(models.Model):
    BOARD_CHOICES = (
        ('person', 'Person'),
        ('product', 'Product'),
        ('place', 'Place'),
    )
    COUNT = (('1', '1'), ('2', '2'),)
    board_count = models.CharField(
        max_length=3, choices=COUNT, blank=True, null=True)
    Category = models.CharField(
        max_length=7, choices=BOARD_CHOICES, blank=True, null=True)
    Project_Name = models.CharField(max_length=50)
    Saved = models.CharField(max_length=50)
    Created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
   # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                         on_delete=models.CASCADE)

    def __str__(self):
        return self.Project_Name
