from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200)
    prof_tag = models.CharField(max_length=2000, default=None, null=True, blank=True)
    email = models.CharField(max_length=200)
    address = models.TextField(max_length=2000, default=None, null=True, blank=True)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000, default=None, null=True, blank=True)
    #degree = models.TextField(max_length=2000, default=None, null=True, blank=True)
    school = models.TextField(max_length=2000, default=None, null=True, blank=True)
    university = models.CharField(max_length=200)
    previous_work = models.TextField(max_length=2000, default=None, null=True, blank=True)
    previous_work_1 = models.TextField(max_length=2000, default=None, null=True, blank=True)
    skills = models.TextField(max_length=1000)
    hobbies = models.TextField(max_length=1000, default=None, null=True, blank=True)
    lang = models.TextField(max_length=1000, default=None, null=True, blank=True)
    
    

    def __str__(self):
        return self.name