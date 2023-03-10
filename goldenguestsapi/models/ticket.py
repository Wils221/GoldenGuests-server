from django.db import models
from django.core.validators import MaxValueValidator



class Ticket(models.Model):

    section = models.IntegerField(validators=[MaxValueValidator(3)])
    number_of_tickets = models.IntegerField(validators=[MaxValueValidator(999)])
    date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    goldenguest = models.ForeignKey("GoldenGuest", on_delete=models.CASCADE)
    opponent = models.ForeignKey("Opponent", on_delete=models.CASCADE)
    