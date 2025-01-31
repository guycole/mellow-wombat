# Generated by Django 4.2.9 on 2025-01-25 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wombat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heeler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bssid', models.CharField(max_length=32)),
                ('ssid', models.CharField(max_length=32)),
                ('frequency', models.CharField(max_length=32)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('ssid',),
            },
        ),
    ]
