from django.db import models
from django.core.validators import MaxValueValidator



class Ticket(models.Model):

    section = models.IntegerField(validators=[MaxValueValidator(3)])
    number_of_tickets = models.IntegerField(validators=[MaxValueValidator(999)])
    date = models.CharField(max_length=15)
    goldenguest = models.ForeignKey("GoldenGuest", on_delete=models.CASCADE)
    opponent = models.ForeignKey("Opponent", on_delete=models.CASCADE)
    isOrgTicket = models.BooleanField(default=False)
    