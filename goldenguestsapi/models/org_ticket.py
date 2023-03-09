from django.db import models



class OrgTicket(models.Model):

    ticket = models.ForeignKey("Ticket", on_delete=models.CASCADE)
    goldenguest = models.ForeignKey("GoldenGuest", on_delete=models.CASCADE)