# Generated by Django 3.2.12 on 2023-09-11 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resnet_core', '0003_alter_info_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='task',
            field=models.CharField(blank=True, default='classification', max_length=50, null=True),
        ),
    ]
