# Generated by Django 5.0 on 2023-12-30 05:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0006_alter_student_student_no_delete_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_no',
            field=models.CharField(default='WPIQBXBAOUAYWLZFJDIFSCKKO605', max_length=30, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge_name', models.CharField(max_length=60)),
                ('date_obtain', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
