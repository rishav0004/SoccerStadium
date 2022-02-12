from django.db import models

# Create your models here.
class Players(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Photo = models.URLField(max_length=200)
    Nationality = models.CharField(max_length=100)
    Flag = models.URLField(max_length=400)
    Overall = models.IntegerField()
    Potential = models.IntegerField()
    Club = models.CharField(max_length=100)
    Value = models.CharField(max_length=10)

    def __str__(self) :
        return self.Name

