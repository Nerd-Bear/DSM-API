# Generated by Django 2.0.13 on 2019-04-24 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0005_auto_20190424_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='appmodel',
            name='app_url',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='appmodel',
            name='description',
            field=models.CharField(max_length=1024),
        ),
    ]
