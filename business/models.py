from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    address = models.TextField()
    owner = models.CharField(max_length=100)
    employee_count = models.IntegerField()
