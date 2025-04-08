from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(_id=ObjectId(), email='crashoverride@mhigh.edu', password='crashoverridepassword'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(name='Blue Team')
        team2 = Team(name='Gold Team')
        team1.save()
        team2.save()
        
        # Assign members to teams manually
        team1.members = users[:3]
        team2.members = users[3:]
        team1.save()
        team2.save()

        # Create activities
        activities = [
            Activity(_id=ObjectId(), name='Cycling', duration=timedelta(hours=1)),
            Activity(_id=ObjectId(), name='Crossfit', duration=timedelta(hours=2)),
            Activity(_id=ObjectId(), name='Running', duration=timedelta(hours=1, minutes=30)),
            Activity(_id=ObjectId(), name='Strength', duration=timedelta(minutes=30)),
            Activity(_id=ObjectId(), name='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), score=100),
            Leaderboard(_id=ObjectId(), score=90),
            Leaderboard(_id=ObjectId(), score=95),
            Leaderboard(_id=ObjectId(), score=85),
            Leaderboard(_id=ObjectId(), score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), description='Cycling Training: Training for a road cycling event'),
            Workout(_id=ObjectId(), description='Crossfit: Training for a crossfit competition'),
            Workout(_id=ObjectId(), description='Running Training: Training for a marathon'),
            Workout(_id=ObjectId(), description='Strength Training: Training for strength'),
            Workout(_id=ObjectId(), description='Swimming Training: Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
