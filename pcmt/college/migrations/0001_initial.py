# Generated by Django 3.0.7 on 2021-02-20 08:39

import college.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('recovery_email', models.EmailField(default='admin@pcmt-india.net', max_length=255)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('enrollment_no', models.CharField(default='', max_length=20)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_HOD', models.BooleanField(default=False)),
                ('is_BOC', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ExamData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('exam', models.IntegerField()),
                ('total_question', models.IntegerField()),
                ('department', models.CharField(default='please enter department', max_length=255)),
                ('semester', models.IntegerField()),
                ('total_marks', models.IntegerField(default=0)),
                ('exam_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('joined_year', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15, verbose_name='phone')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Staff.path_and_rename)),
                ('department', models.CharField(default='', max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('is_HOD', models.BooleanField(default=False)),
                ('is_BOC', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('staff_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField(default='')),
                ('allow_test', models.BooleanField(default=False)),
                ('department', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255, verbose_name='Subject_name')),
                ('subject_code', models.CharField(default='', max_length=255, verbose_name='Subject_code')),
                ('allocated', models.BooleanField(default=False)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Student.path_and_rename)),
                ('department', models.CharField(default='', max_length=255)),
                ('registration_no', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=4)),
                ('semester', models.IntegerField(default=1)),
                ('university_roll', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.CharField(blank=True, default='', max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('present_address', models.CharField(max_length=255)),
                ('permanent_address', models.CharField(max_length=255)),
                ('contact_no', models.CharField(max_length=10, verbose_name='phone')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('blood_group', models.CharField(max_length=3)),
                ('fathers_name', models.CharField(max_length=255)),
                ('fathers_contact_no', models.IntegerField()),
                ('fathers_email', models.EmailField(max_length=100)),
                ('guardian_name', models.CharField(blank=True, max_length=255)),
                ('guardian_contact_no', models.CharField(blank=True, max_length=255)),
                ('relation_with_guardian', models.CharField(blank=True, max_length=255)),
                ('cast', models.CharField(max_length=8)),
                ('admission_category', models.CharField(max_length=15)),
                ('entrance_type', models.CharField(max_length=15)),
                ('rank', models.IntegerField()),
                ('aadhar_no', models.IntegerField()),
                ('school_name_10', models.CharField(blank=True, default='', max_length=255)),
                ('locality_10', models.CharField(blank=True, default='', max_length=255)),
                ('board_10', models.CharField(blank=True, default='', max_length=255)),
                ('medium_10', models.CharField(blank=True, default='', max_length=255)),
                ('marks_10', models.IntegerField(blank=True, default=0)),
                ('total_10', models.IntegerField(blank=True, default=0)),
                ('passing_year_10', models.IntegerField(blank=True, default=0)),
                ('percentage_10', models.IntegerField(blank=True, default=0)),
                ('school_name_12', models.CharField(blank=True, default='', max_length=255)),
                ('locality_12', models.CharField(blank=True, default='', max_length=255)),
                ('board_12', models.CharField(blank=True, default='', max_length=255)),
                ('passing_year_12', models.IntegerField(blank=True, default=0)),
                ('medium_12', models.CharField(blank=True, default='', max_length=255)),
                ('marks_12', models.IntegerField(blank=True, default=0)),
                ('total_12', models.IntegerField(blank=True, default=0)),
                ('percentage_12', models.IntegerField(blank=True, default=0)),
                ('school_name_diploma', models.CharField(blank=True, default='', max_length=255)),
                ('locality_diploma', models.CharField(blank=True, default='', max_length=255)),
                ('board_diploma', models.CharField(blank=True, default='', max_length=255)),
                ('passing_year_diploma', models.IntegerField(blank=True, default=0)),
                ('medium_diploma', models.CharField(blank=True, default='', max_length=255)),
                ('marks_diploma', models.IntegerField(blank=True, default=0)),
                ('total_diploma', models.IntegerField(blank=True, default=0)),
                ('percentage_diploma', models.IntegerField(blank=True, default=0)),
                ('reason', models.CharField(blank=True, default='', max_length=255)),
                ('recovery_email', models.EmailField(default='admin@pcmt-india.net', max_length=255)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
                ('student_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('exam', models.IntegerField()),
                ('department', models.CharField(default='please enter department', max_length=255)),
                ('semester', models.IntegerField()),
                ('marks', models.IntegerField(default=0)),
                ('exam_done', models.BooleanField(default=False)),
                ('exam_date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Subject')),
                ('total_marks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.ExamData')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_no', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('exam', models.IntegerField()),
                ('exam_start_time', models.DateTimeField(default=datetime.datetime(2021, 2, 20, 14, 9, 2, 704083))),
                ('exam_end_time', models.DateTimeField(default=datetime.datetime(2021, 2, 20, 14, 9, 2, 704083))),
                ('question_text', models.CharField(max_length=255)),
                ('choice_text1', models.CharField(max_length=255)),
                ('choice_text2', models.CharField(max_length=255)),
                ('choice_text3', models.CharField(max_length=255)),
                ('choice_text4', models.CharField(max_length=255)),
                ('correct', models.IntegerField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Staff')),
            ],
        ),
        migrations.AddField(
            model_name='examdata',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Subject'),
        ),
        migrations.AddField(
            model_name='examdata',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Staff'),
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_no', models.CharField(default='', max_length=255, unique=True)),
                ('qr_code', models.ImageField(blank=True, upload_to=college.models.Admission.image_qr_code)),
                ('year', models.CharField(max_length=4)),
                ('contact_no', models.CharField(max_length=10, verbose_name='phone')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.CharField(blank=True, default='', max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('state', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('fathers_name', models.CharField(default='', max_length=255)),
                ('mothers_name', models.CharField(default='', max_length=255)),
                ('blood_group', models.CharField(default='', max_length=255)),
                ('mothers_tongue', models.CharField(default='', max_length=255)),
                ('fathers_contact_no', models.CharField(default='', max_length=255)),
                ('fathers_email', models.EmailField(default='', max_length=100)),
                ('guardian_name', models.CharField(blank=True, default='', max_length=255)),
                ('guardian_contact_no', models.CharField(blank=True, default='', max_length=255)),
                ('relation_with_guardian', models.CharField(blank=True, default='', max_length=255)),
                ('nationality', models.CharField(blank=True, max_length=255)),
                ('cast', models.CharField(max_length=8)),
                ('religion', models.CharField(max_length=8)),
                ('physically_challenge', models.CharField(max_length=8)),
                ('department', models.CharField(max_length=255)),
                ('aadhar_card_no', models.CharField(max_length=255)),
                ('aadhar_card', models.ImageField(blank=True, upload_to=college.models.Admission.image_aadhar_card)),
                ('cast_certificate', models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Admission.image_cast_certificate)),
                ('physically_certificate', models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Admission.image_physically_certificate)),
                ('photo', models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Admission.profile)),
                ('admission_cat', models.CharField(max_length=255)),
                ('conducted_by', models.CharField(max_length=255)),
                ('rank', models.CharField(max_length=255)),
                ('roll_no', models.CharField(max_length=255)),
                ('allotment', models.CharField(max_length=10)),
                ('rank_card', models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Admission.rank_card)),
                ('admit_card', models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Admission.admit_card)),
                ('school_name_10', models.CharField(blank=True, default='', max_length=255)),
                ('board_10', models.CharField(blank=True, default='', max_length=255)),
                ('medium_10', models.CharField(blank=True, default='', max_length=255)),
                ('address10', models.CharField(blank=True, default=0, max_length=255)),
                ('city10', models.CharField(blank=True, default=0, max_length=255)),
                ('state10', models.CharField(blank=True, default=0, max_length=255)),
                ('country10', models.CharField(blank=True, default=0, max_length=255)),
                ('passing_year_10', models.CharField(blank=True, default=0, max_length=255)),
                ('sub1', models.CharField(blank=True, default=0, max_length=255)),
                ('sub2', models.CharField(blank=True, default=0, max_length=255)),
                ('sub3', models.CharField(blank=True, default=0, max_length=255)),
                ('sub4', models.CharField(blank=True, default=0, max_length=255)),
                ('sub5', models.CharField(blank=True, default=0, max_length=255)),
                ('aggregate10', models.CharField(blank=True, default='', max_length=255)),
                ('admit10', models.ImageField(blank=True, max_length=255, null=True, upload_to=models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Admission.admit_card))),
                ('mark10', models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Admission.image_marksheet_10)),
                ('certificate10', models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Admission.image_marksheet_10)),
                ('school_name_12', models.CharField(blank=True, default='', max_length=255)),
                ('board_12', models.CharField(blank=True, default='', max_length=255)),
                ('medium_12', models.CharField(blank=True, default='', max_length=255)),
                ('address12', models.CharField(blank=True, default=0, max_length=255)),
                ('city12', models.CharField(blank=True, default=0, max_length=255)),
                ('state12', models.CharField(blank=True, default=0, max_length=255)),
                ('country12', models.CharField(blank=True, default=0, max_length=255)),
                ('passing_year_12', models.CharField(blank=True, default=0, max_length=255)),
                ('english', models.CharField(blank=True, default=0, max_length=255)),
                ('chemistry', models.CharField(blank=True, default=0, max_length=255)),
                ('physics', models.CharField(blank=True, default=0, max_length=255)),
                ('math', models.CharField(blank=True, default=0, max_length=255)),
                ('optional', models.CharField(blank=True, default=0, max_length=255)),
                ('aggregate12', models.CharField(blank=True, default='', max_length=255)),
                ('mark12', models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Admission.image_marksheet_12)),
                ('admit12', models.ImageField(blank=True, max_length=255, null=True, upload_to=models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Admission.admit_card))),
                ('certificate12', models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Admission.image_marksheet_12)),
                ('school_name_diploma', models.CharField(blank=True, default='', max_length=255)),
                ('board_diploma', models.CharField(blank=True, default='', max_length=255)),
                ('medium_diploma', models.CharField(blank=True, default='', max_length=255)),
                ('addressDiploma', models.CharField(blank=True, default=0, max_length=255)),
                ('cityDiploma', models.CharField(blank=True, default=0, max_length=255)),
                ('stateDiploma', models.CharField(blank=True, default=0, max_length=255)),
                ('countryDiploma', models.CharField(blank=True, default=0, max_length=255)),
                ('passing_year_Diploma', models.CharField(blank=True, default=0, max_length=255)),
                ('marksDiploma', models.CharField(blank=True, default='', max_length=255)),
                ('aggregateDiploma', models.CharField(blank=True, default='', max_length=255)),
                ('division', models.CharField(blank=True, default='', max_length=255)),
                ('markDiploma', models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Admission.image_marksheet_diploma)),
                ('certificateDiploma', models.ImageField(blank=True, max_length=255, null=True, upload_to=college.models.Admission.image_certificateDiploma)),
                ('loan', models.CharField(blank=True, default='', max_length=255)),
                ('hostel', models.CharField(blank=True, default='', max_length=255)),
                ('gap', models.CharField(blank=True, default='', max_length=255)),
                ('reason', models.CharField(blank=True, default='', max_length=255)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('joined_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('student_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
