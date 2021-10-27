# Generated by Django 3.2.8 on 2021-10-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='completed',
            new_name='done',
        ),
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
