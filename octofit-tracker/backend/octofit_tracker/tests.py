from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_activity_creation(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        activity = Activity.objects.create(user=user, type='Run', duration=30, calories=300)
        self.assertEqual(activity.type, 'Run')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', duration=20)
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_creation(self):
        user = User.objects.create_user(username='testuser2', password='testpass')
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)
