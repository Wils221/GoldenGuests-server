from django.db import models



class Opponent(models.Model):

    opponent = models.CharField(max_length=25)