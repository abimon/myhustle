# Generated by Django 5.0.1 on 2024-02-06 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediaManage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='desc',
            field=models.CharField(max_length=100, null=True),
        ),
    ]