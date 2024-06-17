# Generated by Django 5.0.2 on 2024-06-14 09:19

import django.db.models.deletion
import status.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0008_remove_complaint_computer'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='computer',
            field=models.ForeignKey(default=status.models.get_default_computer, on_delete=django.db.models.deletion.CASCADE, to='status.computers'),
        ),
    ]