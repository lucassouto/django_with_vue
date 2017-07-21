from django.db import models

class Games(models.Model):
    title = models.CharField(max_length=255)
    plataform = models.CharField(max_length=255)
