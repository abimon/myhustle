# Generated by Django 5.0.1 on 2024-01-29 19:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0004_user_created_at_user_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 29, 19, 18, 37, 113746, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 29, 19, 18, 37, 113746, tzinfo=datetime.timezone.utc)),
        ),
    ]