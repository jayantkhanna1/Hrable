# Generated by Django 4.0.6 on 2022-08-05 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrable_app', '0016_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='hr_comment',
            field=models.CharField(default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='query',
            name='hr_id',
            field=models.CharField(default='Pending', max_length=100),
        ),
    ]
