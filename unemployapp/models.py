from django.db import models
import datetime

# Create your models here.
class Date(models.Model):
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.date.strftime("%m/%d/%Y")

class Application(models.Model):
    #date, company name, location, contact method, type of work sought, results (so dumb)
    date = models.ForeignKey(Date, on_delete=models.PROTECT, related_name="applications")
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    contact_method = models.CharField(max_length=200)
    work_type = models.CharField(max_length=200)
    results = models.CharField(max_length=200) #hired or not hired

    def __str__(self):
        return self.company_name

class Activity(models.Model):
    date = models.ForeignKey(Date, on_delete=models.PROTECT, related_name="activities")
    activity = models.CharField(max_length=200)

    def __str__(self):
        return self.activity