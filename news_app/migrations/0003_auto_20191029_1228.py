# Generated by Django 2.2.6 on 2019-10-29 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_auto_20191029_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(default='user/default.jpg', max_length=255, upload_to='image/user/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(default='Stephen Vasquez', max_length=64, verbose_name='昵称'),
        ),
    ]