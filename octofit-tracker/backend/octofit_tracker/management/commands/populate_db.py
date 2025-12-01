from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create Workouts
        w1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        w2 = Workout.objects.create(name='Running', description='Cardio')

        # Create Activities
        Activity.objects.create(user=ironman, workout=w1, duration=30, calories=200)
        Activity.objects.create(user=captain, workout=w2, duration=45, calories=350)
        Activity.objects.create(user=batman, workout=w1, duration=20, calories=150)
        Activity.objects.create(user=superman, workout=w2, duration=60, calories=500)

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, score=200)
        Leaderboard.objects.create(user=captain, score=350)
        Leaderboard.objects.create(user=batman, score=150)
        Leaderboard.objects.create(user=superman, score=500)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
