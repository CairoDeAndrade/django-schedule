# Generated by Django 4.1 on 2022-09-08 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0002_contact_mostrar"),
    ]

    operations = [
        migrations.RemoveField(model_name="contact", name="mostrar",),
    ]
