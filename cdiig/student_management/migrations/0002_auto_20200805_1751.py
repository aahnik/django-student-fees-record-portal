# Generated by Django 3.0.8 on 2020-08-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feesrecord',
            name='students',
        ),
        migrations.AddField(
            model_name='student',
            name='feesRecords',
            field=models.ManyToManyField(null=True, to='student_management.FeesRecord'),
        ),
    ]
