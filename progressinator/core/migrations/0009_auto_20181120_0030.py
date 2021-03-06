# Generated by Django 2.1.2 on 2018-11-20 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress_core', '0008_auto_20181021_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprogress',
            name='excuse_lateness',
            field=models.CharField(blank=True, choices=[('LATENESS_ABSENT', 'Absent'), ('LATENESS_SICK', 'Sick'), ('LATENESS_PERSONAL', 'Personal'), ('LATENESS_EXCEPTION', 'Exception'), ('LATENESS_NOT_EXCUSED', 'Not excused')], max_length=50, null=True),
        ),
    ]
