# Generated by Django 5.0.2 on 2024-06-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0005_alter_computers_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computers',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]
