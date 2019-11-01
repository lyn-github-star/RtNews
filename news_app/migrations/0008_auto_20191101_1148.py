# Generated by Django 2.2.6 on 2019-11-01 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0007_auto_20191031_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, unique=True, verbose_name='手机')),
                ('code', models.CharField(max_length=8, verbose_name='验证码')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '手机验证',
                'verbose_name_plural': '手机验证',
                'db_table': 'verifycode',
            },
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(default='James Nichols', max_length=64, verbose_name='昵称'),
        ),
    ]