# Generated by Django 3.2 on 2021-04-30 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highest_qualification', models.CharField(max_length=50, verbose_name='highest_qualification')),
                ('dob', models.DateField(verbose_name='date_of_birth')),
                ('employee_code', models.CharField(max_length=50, verbose_name='employee_code')),
                ('employee_grade', models.CharField(max_length=50, verbose_name='employee_grade')),
                ('salary', models.FloatField(verbose_name='salary')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.subject', verbose_name='subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(verbose_name='date_of_birth')),
                ('grade', models.CharField(max_length=50, verbose_name='class')),
                ('section', models.CharField(max_length=50, verbose_name='section')),
                ('roll_no', models.CharField(max_length=50, verbose_name='roll_no')),
                ('admission_no', models.UUIDField(editable=False, verbose_name='admission_no')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
