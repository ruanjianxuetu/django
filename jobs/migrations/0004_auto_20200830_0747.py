# Generated by Django 3.1 on 2020-08-29 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='candidate_introduction',
            field=models.TextField(blank=True, max_length=1024, verbose_name='候选人介绍'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='project_experience',
            field=models.TextField(blank=True, max_length=1024, verbose_name='项目经历'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='work_experience',
            field=models.TextField(blank=True, max_length=1024, verbose_name='工作经历'),
        ),
    ]
