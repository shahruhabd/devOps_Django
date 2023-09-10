from django.db import models
from datetime import datetime

class SinCalculation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    angle = models.FloatField()
    result = models.FloatField()

    def __str__(self):
        return f"Угол {self.angle} = {self.result}"