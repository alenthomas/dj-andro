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

class Team(models.Model):
    team = models.CharField(max_length=40, unique=True)
    short_name = models.CharField(max_length=5, unique=True)
    team_id = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.team_id

class Score(models.Model):
    team = models.ForeignKey(Team)
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.team.team_id + " : " + self.team.short_name
