# Generated by Django 2.2.6 on 2019-10-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(default='Yvonne Weaver', max_length=64, verbose_name='昵称'),
        ),
    ]
