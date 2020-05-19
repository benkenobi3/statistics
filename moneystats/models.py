from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=200)


class Check(models.Model):

    date = models.DateTimeField()


class Expense(models.Model):

    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    date = models.DateTimeField()

    category = models.ForeignKey(Category, related_name='expenses', on_delete=models.CASCADE)
    cash_check = models.ForeignKey(Check, related_name='positions', on_delete=models.CASCADE, null=True)
