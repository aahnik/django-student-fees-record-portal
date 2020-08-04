# Generated by Django 3.0.8 on 2020-08-04 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0002_auto_20200804_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='feesrecord',
            name='month',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student_management.Month'),
        ),
    ]
