# Generated by Django 3.2.14 on 2023-05-24 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApi', '0002_remove_taskmodel_average'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='average',
            field=models.FloatField(null=True),
        ),
    ]
