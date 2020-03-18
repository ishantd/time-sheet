# Generated by Django 3.0.4 on 2020-03-18 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_delete_employeetasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('Process', 'Process'), ('Structure', 'Structure'), ('Piping', 'Piping'), ('Instrumentation', 'Instrumentation'), ('Electrical', 'Electrical'), ('Projects', 'Projects'), ('Mechanical', 'Mechanical'), ('Quality', 'Quality'), ('Documentation', 'Documentation')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField(null=True)),
                ('project_type', models.CharField(choices=[('OH', 'OH'), ('PA', 'PA')], max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_assigned', models.IntegerField(null=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tasks_assignment',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='tasks_assignment',
            name='task',
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('Process', 'Process'), ('Structure', 'Structure'), ('Piping', 'Piping'), ('Instrumentation', 'Instrumentation'), ('Electrical', 'Electrical'), ('Projects', 'Projects'), ('Mechanical', 'Mechanical'), ('Quality', 'Quality'), ('Documentation', 'Documentation')], max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
        migrations.DeleteModel(
            name='Tasks_Assignment',
        ),
        migrations.AddField(
            model_name='projects',
            name='project_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Employee'),
        ),
        migrations.AddField(
            model_name='departments',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Employee'),
        ),
        migrations.AddField(
            model_name='departments',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Projects'),
        ),
    ]
