# Generated by Django 2.1.7 on 2021-02-09 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20210209_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_periods',
            name='end_time',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='activity_periods',
            name='start_time',
            field=models.CharField(max_length=50),
        ),
    ]
