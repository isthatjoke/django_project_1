# Generated by Django 3.1.2 on 2020-11-08 18:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0025_auto_20201031_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 18, 45, 5, 33985, tzinfo=utc)),
        ),
    ]
