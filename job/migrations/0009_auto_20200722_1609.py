# Generated by Django 3.0.8 on 2020-07-22 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_jobapply_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapply',
            old_name='job',
            new_name='job_apply',
        ),
    ]
