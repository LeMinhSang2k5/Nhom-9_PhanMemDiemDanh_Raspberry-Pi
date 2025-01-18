# Generated by Django 5.1.4 on 2025-01-18 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='principal',
            fields=[
                ('name_principal', models.CharField(max_length=255, null=True)),
                ('role', models.CharField(default='Default Role', max_length=255)),
                ('gender', models.BooleanField()),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Principal ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
            ],
        ),
    ]
