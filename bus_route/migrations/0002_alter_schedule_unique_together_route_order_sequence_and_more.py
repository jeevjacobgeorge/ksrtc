# Generated by Django 5.1.6 on 2025-03-07 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_route', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together={('schedule_no', 'trip_no')},
        ),
        migrations.AddField(
            model_name='route',
            name='order_sequence',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='order_sequence',
        ),
    ]
