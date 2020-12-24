from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField(default = False)
    settime = models.PositiveIntegerField()
    passedtime = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.title
# Create your models here.
