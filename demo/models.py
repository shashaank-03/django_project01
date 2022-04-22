from django.db import models

class adduser(models.Model):
    username = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    phone = models.IntegerField()

    def __str__(self):
        return self.username