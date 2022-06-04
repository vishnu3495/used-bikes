from django.db import models

class Bikes(models.Model):
    name=models.CharField(max_length=150)
    registration=models.IntegerField(null=True)
    kilometers=models.PositiveIntegerField(null=True)
    mileage=models.PositiveIntegerField(null=True)
    fuel=models.CharField(max_length=150)
    owners=models.PositiveIntegerField(null=True)



    def __str__(self):
        return self.name