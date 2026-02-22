from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_location', models.CharField(max_length=255)),
                ('end_location', models.CharField(max_length=255)),
                ('distance', models.FloatField()),
                ('status', models.CharField(
                    choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')],
                    default='pending',
                    max_length=20,
                )),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('current_assignment', models.OneToOneField(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='assigned_driver',
                    to='assignments.assignment',
                )),
            ],
        ),
    ]
