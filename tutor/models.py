from django.db import models
from django.utils import timezone

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


class Tutor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.TextField(max_length=999)
    is_tutor_home = models.BooleanField(default=False)
    is_student_home = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Tutor, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.id}_{self.first_name[:3]}_{self.last_name[:5]}'


class Subject(models.Model):
    name = models.CharField(max_length=30)
    name_slug = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    desc = models.TextField(max_length=999, null=True, blank=True)
    
    def __str__(self):
        return f'{self.id}_{self.name_slug}'
