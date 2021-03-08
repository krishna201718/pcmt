# Generated by Django 3.0.7 on 2021-03-05 10:38

import college.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0004_auto_20210305_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='allow_test',
        ),
        migrations.AddField(
            model_name='examdata',
            name='allow_test',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='admission',
            name='admit_card',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Admission.admit_card),
        ),
        migrations.AlterField(
            model_name='admission',
            name='rank_card',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Admission.rank_card),
        ),
        migrations.AlterField(
            model_name='question',
            name='exam_end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 5, 16, 8, 16, 433024)),
        ),
        migrations.AlterField(
            model_name='question',
            name='exam_start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 5, 16, 8, 16, 433024)),
        ),
        migrations.AlterField(
            model_name='student',
            name='admit_card',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Student.admit_card),
        ),
        migrations.AlterField(
            model_name='student',
            name='rank_card',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Student.rank_card),
        ),
    ]
