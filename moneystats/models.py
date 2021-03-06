from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Check(models.Model):

    date = models.DateTimeField()


class Expense(models.Model):

    name = models.CharField(max_length=200)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, related_name='expenses', on_delete=models.CASCADE)

    category = models.ForeignKey(Category, related_name='expenses', on_delete=models.CASCADE)
    cash_check = models.ForeignKey(Check, related_name='positions', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
