# Generated by Django 2.1.5 on 2019-02-28 13:50

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCentre', '0002_auto_20190227_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningcentresubcategoriesquestionanswer',
            name='answer',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='learningcentresubcategoriesquestionanswer',
            name='question',
            field=models.CharField(max_length=10000000),
        ),
    ]