from django.core.management.base import BaseCommand
from assignments.models import Assignment, Driver


ASSIGNMENTS = [
    {'start_location': 'Chicago, IL', 'end_location': 'Detroit, MI', 'distance': 281.0, 'status': 'pending'},
    {'start_location': 'Detroit, MI', 'end_location': 'Cleveland, OH', 'distance': 169.0, 'status': 'in_progress'},
    {'start_location': 'Cleveland, OH', 'end_location': 'Pittsburgh, PA', 'distance': 131.0, 'status': 'pending'},
    {'start_location': 'Pittsburgh, PA', 'end_location': 'Philadelphia, PA', 'distance': 305.0, 'status': 'completed'},
    {'start_location': 'Philadelphia, PA', 'end_location': 'New York, NY', 'distance': 95.0, 'status': 'pending'},
]

DRIVERS = [
    {'first_name': 'Alice', 'last_name': 'Johnson'},
    {'first_name': 'Bob', 'last_name': 'Martinez'},
    {'first_name': 'Carol', 'last_name': 'Williams'},
    {'first_name': 'David', 'last_name': 'Lee'},
]


class Command(BaseCommand):
    help = 'Seed the database with demo assignments and drivers'

    def handle(self, *args, **options):
        Driver.objects.all().delete()
        Assignment.objects.all().delete()

        assignments = [Assignment.objects.create(**a) for a in ASSIGNMENTS]
        self.stdout.write(f'Created {len(assignments)} assignments.')

        drivers = [Driver.objects.create(**d) for d in DRIVERS]
        self.stdout.write(f'Created {len(drivers)} drivers.')

        # Assign first two drivers to first two assignments
        drivers[0].current_assignment = assignments[0]
        drivers[0].save()
        drivers[1].current_assignment = assignments[1]
        drivers[1].save()

        self.stdout.write(self.style.SUCCESS('Demo data seeded successfully.'))
