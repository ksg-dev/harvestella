# Generated by Django 4.1.7 on 2023-03-16 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='season',
        ),
    ]
