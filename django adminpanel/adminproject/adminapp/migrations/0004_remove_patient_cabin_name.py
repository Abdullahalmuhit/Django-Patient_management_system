# Generated by Django 2.1.2 on 2019-06-24 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_auto_20190624_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='cabin_name',
        ),
    ]
