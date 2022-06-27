from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=5)
    
    def __str__(self):
        return f'{self.id}_{self.name}'


class City(models.Model):
    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}_{self.name}'
