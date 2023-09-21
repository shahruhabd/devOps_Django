# Generated by Django 4.2.5 on 2023-09-20 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HelpDesk", "0003_alter_request_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="request",
            name="status",
            field=models.CharField(
                choices=[
                    ("NEW", "new"),
                    ("IN PROGRESS", "in progress"),
                    ("RESOLVED", "resolved"),
                ],
                default="NEW",
                max_length=11,
            ),
        ),
    ]
