# Generated by Django 3.2 on 2021-04-30 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Subject')),
                ('code', models.CharField(max_length=50, verbose_name='code')),
                ('subject_type', models.CharField(choices=[('TH', 'Theory'), ('PR', 'Practical')], max_length=50, verbose_name='subject_type')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=50, verbose_name='Grade')),
                ('class_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='class_teacher')),
                ('subjects', models.ManyToManyField(to='curriculum.Subject', verbose_name='Grades')),
            ],
        ),
    ]
