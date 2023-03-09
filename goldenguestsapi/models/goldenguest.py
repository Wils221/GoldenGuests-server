from django.db import models
from django.contrib.auth.models import User


class GoldenGuest(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isTicketHolder = models.BooleanField(null=False)