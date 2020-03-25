from django.db import models

class User(models.Model):
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=255)
    daily_working_hours = models.IntegerField()
    monthly_working_days = models.IntegerField()

    def __str__(self):
        return self.name
