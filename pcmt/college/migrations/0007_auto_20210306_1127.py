# Generated by Django 3.0.7 on 2021-03-06 05:57

import college.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0006_auto_20210306_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='ca_marks1',
            new_name='ca1_marks',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='ca_marks2',
            new_name='ca2_marks',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='ca_marks3',
            new_name='ca3_marks',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='ca_marks4',
            new_name='ca4_marks',
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
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 6, 11, 26, 58, 303853)),
        ),
        migrations.AlterField(
            model_name='question',
            name='exam_start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 6, 11, 26, 58, 303853)),
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
