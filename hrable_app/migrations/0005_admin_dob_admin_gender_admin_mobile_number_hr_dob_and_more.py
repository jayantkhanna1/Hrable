# Generated by Django 4.0.6 on 2022-07-26 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrable_app', '0004_refferal_name_of_referrer'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='dob',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin',
            name='gender',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin',
            name='mobile_number',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hr',
            name='dob',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hr',
            name='gender',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hr',
            name='mobile_number',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job_application',
            name='gender',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
