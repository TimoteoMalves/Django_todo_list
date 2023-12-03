# Generated by Django 4.2.7 on 2023-12-03 19:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_task_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['complete', 'priority']},
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
