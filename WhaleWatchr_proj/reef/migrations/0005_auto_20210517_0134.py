# Generated by Django 3.1.7 on 2021-05-17 05:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reef', '0004_auto_20210516_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(default='password', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='updaterequest',
            name='start_date',
            field=models.DateField(default=datetime.date(2021, 5, 17)),
        ),
    ]
