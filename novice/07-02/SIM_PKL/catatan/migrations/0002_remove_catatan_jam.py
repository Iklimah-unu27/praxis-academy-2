# Generated by Django 3.1.2 on 2020-10-13 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catatan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catatan',
            name='jam',
        ),
    ]
