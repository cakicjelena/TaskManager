# Generated by Django 5.0.1 on 2024-02-14 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagerAPI', '0002_alter_user_is_active_alter_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectId', models.IntegerField()),
                ('taskId', models.IntegerField()),
                ('projectName', models.CharField(max_length=100)),
                ('taskName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserOnProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectId', models.IntegerField()),
                ('userId', models.IntegerField()),
                ('projectName', models.CharField(max_length=100)),
                ('userName', models.CharField(max_length=100)),
                ('startDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserOnTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskId', models.IntegerField()),
                ('userId', models.IntegerField()),
                ('taskName', models.CharField(max_length=100)),
                ('userName', models.CharField(max_length=100)),
                ('startDate', models.DateField()),
            ],
        ),
    ]