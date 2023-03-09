from django.db import models



class Ticket(models.Model):

    section = models.IntegerField(max_length=4)
    number_of_tickets = models.IntegerField(max_length=3)
    date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    goldenguest = models.ForeignKey("GoldenGuest", on_delete=models.CASCADE)
    opponent = models.ForeignKey("Opponent", on_delete=models.CASCADE)
    