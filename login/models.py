from django.db import models

class Login(models.Model):
    email_id = models.EmailField(max_length=40, unique=True)
    password = models.CharField(max_length=35)
    mobile_number = models.CharField(max_length=13, unique=True)
    hint = models.CharField(max_length=40)

    def __str__(self):
        return self.email_id

class About(models.Model):

    about = models.TextField(max_length=100)

    def __str__(self):
        return str(self.id)
