# Generated by Django 5.0 on 2024-01-21 04:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0003_course_course_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
