from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    phone = models.CharField(max_length=20, blank=True, null=True)
    birth = models.DateField()

    def __str__(self):
        return self.user.username

