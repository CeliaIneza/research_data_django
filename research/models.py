from django.db import models

# Create your models here.

class Researcher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contacts = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True) 
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ResearchProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    researchers = models.ManyToManyField(Researcher)

    def __str__(self):
        return self.title
