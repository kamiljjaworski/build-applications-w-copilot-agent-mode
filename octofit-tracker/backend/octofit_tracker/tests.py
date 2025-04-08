from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", password="password123")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team A")
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(name="Running", duration="00:30:00")
        self.assertEqual(activity.name, "Running")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(description="Push-ups")
        self.assertEqual(workout.description, "Push-ups")
