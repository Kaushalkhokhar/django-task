from django.db import models
from user.models import MyUser
from doctor.models import Doctor

class Patient(MyUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
