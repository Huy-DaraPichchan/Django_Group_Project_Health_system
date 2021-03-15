from django.db import models

class Covid_Report(models.Model):
    country = models.TextField()
    in_treatmeant = models.IntegerField(default=0)
    treated = models.IntegerField(default=0)
    death = models.IntegerField(default=0)
class Symptom_Analysis(models.Model):
    q1 = models.BooleanField()
    q2 = models.BooleanField()
    q3 = models.BooleanField()
    q4 = models.BooleanField()
    q5 = models.BooleanField()
