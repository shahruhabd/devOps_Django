from django.db import models

class Game(models.Model):
    secret_number = models.IntegerField()
    attempts = models.IntegerField(default=0)
