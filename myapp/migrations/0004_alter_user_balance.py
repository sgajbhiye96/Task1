# Generated by Django 3.2.12 on 2022-04-11 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Balance',
            field=models.IntegerField(),
        ),
    ]
