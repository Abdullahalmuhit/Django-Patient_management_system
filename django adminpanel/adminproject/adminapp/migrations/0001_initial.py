# Generated by Django 2.1.2 on 2019-06-23 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_picture', models.FileField(upload_to='')),
                ('details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('admited_on', models.DateTimeField(auto_now_add=True)),
                ('release_on', models.DateTimeField(auto_now_add=True)),
                ('cabin_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Cabin')),
                ('nurse_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Nurse')),
            ],
        ),
        migrations.AddField(
            model_name='cabin',
            name='nurse_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Nurse'),
        ),
    ]
