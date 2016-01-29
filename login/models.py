from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class Comments(models.Model):
    username = models.ForeignKey(Users)
    title = models.CharField(max_length=25)
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.title
