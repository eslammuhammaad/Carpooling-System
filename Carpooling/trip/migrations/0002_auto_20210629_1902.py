# Generated by Django 3.2.4 on 2021-06-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userTrips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('tripId', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='tripId',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='trip',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='distanceTravelled',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='endLatitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='endLongitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='endTime',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='startLatitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='startLongitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='startTime',
            field=models.FloatField(),
        ),
    ]
