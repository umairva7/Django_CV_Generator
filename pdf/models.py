from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=100, blank=True, null=True)
    collage = models.CharField(max_length=100, blank=True, null=True)
    university = models.CharField(max_length=100, blank=True, null=True)
    year_of_completion = models.IntegerField(blank=True, null=True)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    summary = models.TextField()
    experience = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    education = models.ForeignKey(Education, on_delete=models.SET_NULL, blank=True, null=True)  # Make it optional
