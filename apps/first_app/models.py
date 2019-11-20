from __future__ import unicode_literals
from django.db import models
from apps.logreg.models import *





class MessageManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['mess']) < 3:
            errors['mess'] = "Message must have more than 3 characters."
        return errors


class Message(models.Model):
    message = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='messages')
    objects = MessageManager()
    def __repr__(self):
        return f"<Movie object: {self.message} ({self.id})>"

# Create your models here.

