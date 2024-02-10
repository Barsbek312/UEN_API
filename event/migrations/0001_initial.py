# Generated by Django 4.2.4 on 2024-02-07 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("place", models.CharField(max_length=300)),
                ("capacity", models.IntegerField(default=0)),
                ("description", models.TextField()),
                ("status", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="EventFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="event_files/")),
            ],
        ),
        migrations.CreateModel(
            name="EventImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="event_images/")),
            ],
        ),
        migrations.CreateModel(
            name="EventVideo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("video", models.FileField(upload_to="event_videos/")),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="event_video",
                        to="event.event",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EventInvitations",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CS", "Consideration"),
                            ("RJ", "Rejected"),
                            ("AC", "Accepted"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="event_invitation",
                        to="event.event",
                    ),
                ),
            ],
        ),
    ]