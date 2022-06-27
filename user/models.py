from django.db import models
from django.utils import timezone
from tutor.models import City


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.id}_{self.first_name[:3]}_{self.last_name[:5]}'