from user.models import MyUser
from django.db import models

class Doctor(MyUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

