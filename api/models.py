from django.db import models
from rest_framework.authtoken.models import Token


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
    passed_by = models.CharField(max_length=50)
