# Generated by Django 3.2 on 2023-12-04 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Additionalitem',
            fields=[
                ('additionalitem_id', models.AutoField(primary_key=True, serialize=False)),
                ('aitm_item', models.CharField(max_length=255)),
                ('aitm_itemdesc', models.CharField(blank=True, max_length=255, null=True)),
                ('aitm_cost', models.IntegerField()),
            ],
            options={
                'db_table': 'additionalitem',
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
            name='Passenger',
            fields=[
                ('passenger_id', models.AutoField(primary_key=True, serialize=False)),
                ('pax_lname', models.CharField(max_length=255)),
                ('pax_fname', models.CharField(max_length=255)),
                ('pax_birthdate', models.DateField()),
            ],
            options={
                'db_table': 'passenger',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('bkg_passenger', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='FlightBooking.passenger')),
            ],
            options={
                'db_table': 'booking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BookingAdditionalitem',
            fields=[
                ('bai_passenger', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='FlightBooking.passenger')),
                ('bai_quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'booking_additionalitem',
                'managed': False,
            },
        ),
    ]