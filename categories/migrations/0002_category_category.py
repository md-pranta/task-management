# Generated by Django 4.2.7 on 2023-12-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_task_category'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.ManyToManyField(to='tasks.task'),
        ),
    ]