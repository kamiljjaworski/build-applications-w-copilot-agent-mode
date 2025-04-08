from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, unique=True)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)

class Activity(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    duration = models.DurationField()

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    score = models.IntegerField()

class Workout(models.Model):
    _id = models.ObjectIdField()
    description = models.TextField()
