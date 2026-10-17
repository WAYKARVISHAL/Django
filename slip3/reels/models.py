from django.db import models

# Create your models here.
class Reel(models.Model):
    reel_name=models.CharField(max_length=100)
    caption=models.CharField(max_length=200)

    def __str__(self):
        return self.reel_name

