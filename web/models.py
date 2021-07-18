from django.db import models
from django.contrib import admin

# Create your models here.

class SubscribedMail(models.Model):
    email = models.EmailField(max_length=254)
    def __str__(self):
        return f"{self.email}"

class UserQuery(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=13)
    Contact_us = 'CU'
    Suggest_us = 'SU'
    Volunteer_with_us = 'VU'
    Query_choices = [
        (Contact_us, 'Contact Us'),
        (Suggest_us, 'Suggest Us'),
        (Volunteer_with_us, 'Volunteer With Us'),
    ]
    query = models.CharField(
        max_length=2,
        choices=Query_choices,
    )
    comments = models.TextField()
    subscribe_to_mail = models.BooleanField()
    subscribe_to_whatsapp = models.BooleanField()

    def __str__(self):
        return f"{self.name} wants to {self.query}"


class PastEvent(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=250)
    description = models.TextField()
    main_image = models.ImageField(upload_to="web/images", default="")
    def __str__(self):
        return f"{self.pk}. {self.title}"

class UpcomingEvent(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=250)
    description = models.TextField()
    main_image = models.ImageField(upload_to="web/images", default="")
    def __str__(self):
        return f"{self.pk}. {self.title}"
