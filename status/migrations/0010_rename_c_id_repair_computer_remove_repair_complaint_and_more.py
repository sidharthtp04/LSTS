# Generated by Django 5.0.2 on 2024-06-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0009_complaint_computer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repair',
            old_name='c_id',
            new_name='computer',
        ),
        migrations.RemoveField(
            model_name='repair',
            name='complaint',
        ),
        migrations.AddField(
            model_name='repair',
            name='reason',
            field=models.TextField(default='Not specified'),
        ),
    ]