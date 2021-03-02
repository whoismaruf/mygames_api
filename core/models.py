from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=250, blank=False)
    is_purchased = models.BooleanField(default=False)
    added_date = models.DateTimeField(default=timezone.now)
    gamer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
