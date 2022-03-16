# Generated by Django 3.2.12 on 2022-03-16 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('active', models.BooleanField()),
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
