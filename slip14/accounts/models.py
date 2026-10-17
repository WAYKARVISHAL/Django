from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    balance = models.FloatField()

    def __str__(self):
        return self.name