# Generated by Django 3.2.8 on 2021-10-31 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='source_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
