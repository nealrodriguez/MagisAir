# Generated by Django 3.2 on 2023-12-04 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrewAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'crew_assignment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CrewMember',
            fields=[
                ('crew_id', models.AutoField(primary_key=True, serialize=False)),
                ('crw_lname', models.CharField(max_length=255)),
                ('crw_fname', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'crew_member',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('flt_datetime_departure', models.DateTimeField()),
                ('flt_datetime_arrival', models.DateTimeField()),
            ],
            options={
                'db_table': 'flight',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('rle_title', models.CharField(max_length=255)),
                ('rle_desc', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'role',
                'managed': False,
            },
        ),
    ]