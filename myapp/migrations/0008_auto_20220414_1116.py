# Generated by Django 3.2.12 on 2022-04-14 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20220411_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='balance',
        ),
        migrations.CreateModel(
            name='balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
