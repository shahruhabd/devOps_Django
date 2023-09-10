from django.db import models

class Game(models.Model):
    secret_number = models.IntegerField()
    attempts = models.IntegerField(default=0)
    is_guessed = models.BooleanField(default=False)
