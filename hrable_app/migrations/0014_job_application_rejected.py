# Generated by Django 4.0.6 on 2022-08-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrable_app', '0013_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Application_Rejected',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=100)),
                ('job_id', models.CharField(max_length=100)),
                ('cover_letter', models.CharField(max_length=10000)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
    ]
