# Generated by Django 3.2.13 on 2023-09-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_guessed',
            field=models.BooleanField(default=False),
        ),
    ]