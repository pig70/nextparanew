# Generated by Django 2.1.4 on 2019-01-04 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_authorprofile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorprofile',
            name='gender',
        ),
    ]