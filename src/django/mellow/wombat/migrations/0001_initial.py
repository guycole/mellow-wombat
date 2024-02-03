# Generated by Django 4.2.9 on 2024-01-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('slot', models.IntegerField()),
                ('event', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='GeoLoc',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time_stamp', models.BigIntegerField()),
                ('latitude', models.CharField(max_length=16)),
                ('longitude', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='ShelfInventory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('power', models.BooleanField()),
                ('slot', models.IntegerField()),
                ('shelf_type', models.IntegerField()),
                ('description', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Tasking',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time_stamp', models.BigIntegerField()),
            ],
        ),
    ]