# Generated by Django 3.0.8 on 2020-07-22 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20200722_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='job_apply_cv/')),
                ('discription', models.TextField()),
                ('apply_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
