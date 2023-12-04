# Generated by Django 3.2 on 2023-12-02 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('loc_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.AutoField(primary_key=True, serialize=False)),
                ('rt_price', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'route',
                'managed': False,
            },
        ),
    ]
