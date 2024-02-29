# Generated by Django 5.0.2 on 2024-02-08 09:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cpu_types',
            fields=[
                ('cpu_id', models.AutoField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=15)),
                ('generation', models.CharField(max_length=15)),
                ('speed', models.IntegerField()),
                ('series', models.CharField(max_length=20)),
                ('core_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='keyboard',
            fields=[
                ('keyboard_id', models.AutoField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='lab',
            fields=[
                ('lab_id', models.AutoField(primary_key=True, serialize=False)),
                ('lab_name', models.CharField(max_length=15)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='monitor',
            fields=[
                ('monitor_id', models.AutoField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=15)),
                ('size', models.CharField(max_length=15)),
                ('resolution', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='motherboard_type',
            fields=[
                ('mb_id', models.AutoField(primary_key=True, serialize=False)),
                ('mb_socket_type', models.CharField(max_length=15)),
                ('max_ram_capacity', models.CharField(max_length=15)),
                ('make', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='mouse',
            fields=[
                ('mouse_id', models.AutoField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='programme',
            fields=[
                ('programme_id', models.AutoField(primary_key=True, serialize=False)),
                ('programme_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ram_type',
            fields=[
                ('ram_id', models.AutoField(primary_key=True, serialize=False)),
                ('ram_size', models.CharField(max_length=15)),
                ('make', models.CharField(max_length=15)),
                ('speed', models.IntegerField()),
                ('series', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='smps',
            fields=[
                ('smps_id', models.AutoField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=15)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='storage_type',
            fields=[
                ('storage_id', models.AutoField(primary_key=True, serialize=False)),
                ('storage_size', models.CharField(max_length=15)),
                ('make', models.CharField(max_length=15)),
                ('technology', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='lab_timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('hour', models.TimeField()),
                ('year', models.IntegerField()),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.lab')),
                ('programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.programme')),
            ],
        ),
        migrations.CreateModel(
            name='computers',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_label', models.CharField(max_length=20)),
                ('dop', models.DateField()),
                ('status', models.CharField(max_length=20)),
                ('invoice_no', models.IntegerField()),
                ('os_type', models.CharField(max_length=20)),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.cpu_types')),
                ('keyboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.keyboard')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.lab')),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.monitor')),
                ('mb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.motherboard_type')),
                ('mouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.mouse')),
                ('ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.ram_type')),
                ('smps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.smps')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.storage_type')),
            ],
        ),
        migrations.CreateModel(
            name='repair',
            fields=[
                ('repair_id', models.AutoField(primary_key=True, serialize=False)),
                ('complaint', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('complaint_date', models.DateField()),
                ('repair_cost', models.IntegerField()),
                ('technician_address', models.TextField()),
                ('repair_date', models.DateField()),
                ('invoice_no', models.IntegerField()),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.computers')),
            ],
        ),
    ]
