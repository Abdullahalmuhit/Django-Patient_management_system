# Generated by Django 2.1.2 on 2019-06-27 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_auto_20190627_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cabin',
            name='nurse_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='cabin_name',
        ),
    ]
