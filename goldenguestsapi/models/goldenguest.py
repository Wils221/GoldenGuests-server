from django.db import models
from django.contrib.auth.models import User


class GoldenGuest(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=50, blank=True, null=True)
    isTicketHolder = models.BooleanField(null=True, default=False)


    property
    def first_name(self):
        return f'{self.user.first_name}'
    
    property
    def email(self):
        return f'{self.user.email}'