# Generated by Django 4.2.13 on 2024-06-29 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('complaint_details', models.TextField()),
                ('complaint_date', models.DateField(auto_now_add=True)),
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
            ],
        ),
        migrations.CreateModel(
            name='cpu_types',
            fields=[
                ('cpu_id', models.AutoField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=15)),
                ('generation', models.CharField(max_length=15)),
                ('speed', models.CharField(max_length=15)),
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
            name='Repair',
            fields=[
                ('repair_id', models.AutoField(primary_key=True, serialize=False)),
                ('reason', models.TextField()),
                ('repair_date', models.DateField(auto_now_add=True)),
                ('complaint', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='status.complaint')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.computers')),
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
        migrations.AddField(
            model_name='computers',
            name='cpu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.cpu_types'),
        ),
        migrations.AddField(
            model_name='computers',
            name='keyboard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.keyboard'),
        ),
        migrations.AddField(
            model_name='computers',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.lab'),
        ),
        migrations.AddField(
            model_name='computers',
            name='mb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.motherboard_type'),
        ),
        migrations.AddField(
            model_name='computers',
            name='monitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.monitor'),
        ),
        migrations.AddField(
            model_name='computers',
            name='mouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.mouse'),
        ),
        migrations.AddField(
            model_name='computers',
            name='ram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.ram_type'),
        ),
        migrations.AddField(
            model_name='computers',
            name='smps',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.smps'),
        ),
        migrations.AddField(
            model_name='computers',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.storage_type'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='computer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.computers'),
        ),
    ]
