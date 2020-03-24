from django.db import models

class User(models.Model):
    email = models.CharField()
    name = models.CharField()
    password = models.CharField()
