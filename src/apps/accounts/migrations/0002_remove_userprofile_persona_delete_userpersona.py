# Generated by Django 4.2.5 on 2023-10-15 17:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="persona",
        ),
        migrations.DeleteModel(
            name="UserPersona",
        ),
    ]
