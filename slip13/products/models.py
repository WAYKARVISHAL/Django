from django.db import models

class Product(models.Model):
    Pname = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.FloatField()

    def __str__(self):
        return self.Pname