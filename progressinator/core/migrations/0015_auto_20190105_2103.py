# Generated by Django 2.1.2 on 2019-01-05 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress_core', '0014_auto_20190105_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='current_section',
            field=models.CharField(blank=True, choices=[('010', '010'), ('020', '020'), ('030', '030'), ('040', '040')], max_length=3, null=True),
        ),
    ]
