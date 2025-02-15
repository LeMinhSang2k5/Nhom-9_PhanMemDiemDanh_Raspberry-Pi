# Generated by Django 5.1.5 on 2025-02-12 15:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='history_attendance',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('student_id', models.CharField(max_length=50, unique=True)),
                ('class_name', models.CharField(max_length=100)),
                ('checkin_time', models.TimeField(blank=True, null=True)),
                ('checkout_time', models.TimeField(blank=True, null=True)),
                ('date_attendance', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late'), ('excused', 'Excused')], default='present', max_length=20)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-date_attendance'],
            },
        ),
        migrations.CreateModel(
            name='principals',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Principal ID')),
                ('name_principal', models.CharField(max_length=255, null=True)),
                ('role', models.CharField(default='Default Role', max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name_student', models.CharField(max_length=255)),
                ('student_id', models.CharField(max_length=50, unique=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('contactPH', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='teachers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name_teacher', models.CharField(max_length=255, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('teacher_id', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('contact', models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]
