from django.db import models

# Create your models here.


class Operation(models.Model):
    operacion = models.CharField(max_length=32)
    numero_1 = models.FloatField()
    numero_2 = models.FloatField()
