# Generated by Django 5.1.4 on 2024-12-20 20:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pdf", "0003_delete_profile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Education",
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
                ("degree", models.CharField(max_length=100)),
                ("school", models.CharField(max_length=100)),
                ("collage", models.CharField(max_length=100)),
                ("university", models.CharField(max_length=100)),
                ("year_of_completion", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("number", models.CharField(max_length=15)),
                ("summary", models.TextField(max_length=500)),
                ("experience", models.CharField(max_length=500)),
                ("skills", models.CharField(max_length=1000)),
                (
                    "education",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profiles",
                        to="pdf.education",
                    ),
                ),
            ],
        ),
    ]