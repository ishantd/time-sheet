# Generated by Django 3.0.4 on 2020-03-18 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200318_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='time_allocated',
            field=models.IntegerField(null=True),
        ),
    ]