# Generated by Django 3.0.4 on 2020-03-18 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_employeetasks_task'),
    ]

    operations = [
        migrations.DeleteModel(
            name='employeeTasks',
        ),
    ]