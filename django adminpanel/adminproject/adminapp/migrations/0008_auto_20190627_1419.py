# Generated by Django 2.1.2 on 2019-06-27 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_auto_20190627_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabin',
            name='nurse_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminapp.Nurse'),
        ),
        migrations.AddField(
            model_name='patient',
            name='cabin_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminapp.Cabin'),
        ),
    ]
