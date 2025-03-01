# Generated by Django 5.1.6 on 2025-02-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('progress', 'Progress'), ('completed', 'Completed')], default='Pending', max_length=9),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(help_text='Describe what the task is', max_length=300),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(help_text='What is the name of your task?', max_length=100),
        ),
    ]
