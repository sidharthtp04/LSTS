# Generated by Django 5.0.6 on 2024-06-12 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("status", "0008_alter_computers_keyboard"),
    ]

    operations = [
        migrations.RenameField(
            model_name="repair",
            old_name="c_id",
            new_name="computer",
        ),
        migrations.CreateModel(
            name="Complaint",
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
                ("complaint_details", models.CharField(max_length=50)),
                ("complaint_date", models.DateField()),
                (
                    "computer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="computer_complaints",
                        to="status.computers",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="computer_status_complaints",
                        to="status.computers",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="repair",
            name="complaint_date",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="status.complaint"
            ),
        ),
    ]