# Generated by Django 4.1 on 2022-09-19 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0006_rename_photo_contact_image"),
    ]

    operations = [
        migrations.RemoveField(model_name="contact", name="image",),
    ]