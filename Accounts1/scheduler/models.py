from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    """Creating a database for the Activity model """
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=140)
    approx_time = models.IntegerField(null=True)
    due_date = models.DateField()
    priority = models.IntegerField(default=0)

    """Setting title as the string to control how the article is going 
    to look when we use shell and in the admin section"""
    def __str__(self):
        return self.title

class Frees(models.Model):
     """Creating a database for the Frees model 
     (forces new users to sign in before clicking into other pages) """
    startTime = models.DateTimeField()
    finishTime = models.DateTimeField()