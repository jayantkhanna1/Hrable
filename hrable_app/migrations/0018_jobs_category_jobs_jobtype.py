# Generated by Django 4.0.6 on 2022-08-07 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrable_app', '0017_query_hr_comment_alter_query_hr_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='category',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobs',
            name='jobtype',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
