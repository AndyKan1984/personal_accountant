from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Income(models.Model):
    amount = models.BigIntegerField()
    time = models.DateTimeField()
    note = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Expense(models.Model):
    amount = models.BigIntegerField()
    time = models.DateTimeField()
    note = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Token(models.Model):
    token = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
