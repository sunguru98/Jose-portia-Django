# Generated by Django 2.1.2 on 2018-11-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptwo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
    ]
