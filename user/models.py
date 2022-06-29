from django.db import models
from django.utils import timezone
from tutor.models import City, Tutor


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


class Mark(models.Model):
    MARKS_LIST = (
        (1, 'Failure'),
        (2, 'Bad'),
        (3, 'Satisfactorily'),
        (4, 'Good'),
        (5, 'Great'),
    )

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    mark = models.CharField(max_length=1, choices=MARKS_LIST, default=5)
    created = models.DateTimeField(editable=False)
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        return super(Mark, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.id}_{self.tutor}'
