# Generated by Django 4.1 on 2022-08-07 02:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0004_alter_note_model_note_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note_model',
            name='note_desc',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
