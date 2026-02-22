from django.db import models


class Assignment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    distance = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.start_location} → {self.end_location}"


class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    current_assignment = models.OneToOneField(
        Assignment,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='assigned_driver',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
