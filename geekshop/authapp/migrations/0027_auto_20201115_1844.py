# Generated by Django 3.1.2 on 2020-11-15 15:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0026_auto_20201108_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 17, 15, 44, 54, 275521, tzinfo=utc)),
        ),
    ]
