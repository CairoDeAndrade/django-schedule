# Generated by Django 4.1 on 2022-09-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0003_remove_contact_mostrar"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact", name="show", field=models.BooleanField(default=True),
        ),
    ]
