# Generated by Django 4.0.6 on 2022-07-31 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrable_app', '0006_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_application',
            name='jobname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]