# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.db import models

class Score(models.Model):
    player_name = models.CharField(max_length=100)
    score = models.IntegerField()