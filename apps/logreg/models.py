from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name cannot be less than 2 Characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name cannot be less than 2 Characters"
        email = postData['email']
        if '@' not in email:
            errors['email'] = "Must be a valid email"
        if '.com' not in email:
            errors['email'] = "Must be a valid email"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        return errors




class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    objects = UserManager()



# First Name - required; at least 2 characters; letters only
# Last Name - required; at least 2 characters; letters only
# Email - required; valid format
# Password - required; at least 8 characters; matches password confirmation
# Create your models here.
