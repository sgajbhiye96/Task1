# Generated by Django 3.2.12 on 2022-04-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20220411_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Balance',
            field=models.IntegerField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
