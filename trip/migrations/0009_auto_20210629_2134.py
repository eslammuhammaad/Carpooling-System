# Generated by Django 3.2.4 on 2021-06-29 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0008_auto_20210629_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='userTrips',
        ),
        migrations.AddField(
            model_name='trip',
            name='userId',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]