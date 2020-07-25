from django.db import models


class Place(models.Model):
    city = models.CharField(max_length=100)
    view = models.BooleanField(default=False)


