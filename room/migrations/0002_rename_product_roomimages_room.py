# Generated by Django 5.0.1 on 2024-02-25 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomimages',
            old_name='product',
            new_name='room',
        ),
    ]