# Generated by Django 2.1.5 on 2019-02-27 07:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20190227_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdetailtoday',
            name='today',
            field=models.CharField(default=datetime.datetime(2019, 2, 27, 7, 24, 20, 537089), max_length=100),
        ),
    ]
