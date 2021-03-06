# Generated by Django 2.2.6 on 2019-10-29 11:18

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(default='U', max_length=64, verbose_name='昵称')),
                ('gender', models.CharField(choices=[('0', '女'), ('1', '男'), ('2', '保密')], default=2, max_length=1, verbose_name='性别')),
                ('birthday', models.DateField(null=True, verbose_name='生日')),
                ('mobile', models.CharField(max_length=11, null=True, verbose_name='电话')),
                ('image', models.ImageField(default='user/default.jpg', max_length=255, upload_to='user/%Y/%m')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'user_info',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='类型编号')),
                ('name', models.CharField(max_length=64, verbose_name='姓名')),
            ],
            options={
                'verbose_name': '新闻类型',
                'verbose_name_plural': '新闻类型',
                'db_table': 'news_type',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('picture', models.CharField(max_length=128, verbose_name='标签')),
                ('content', models.TextField()),
                ('image', models.ImageField(default='content/default.jpg', max_length=255, upload_to='image/content/%Y/%m%d', verbose_name='封面图片')),
                ('publish_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='生成时间')),
                ('clicked', models.IntegerField(default=0, verbose_name='点击量')),
                ('is_deleted', models.BooleanField(default=0, verbose_name='是否删除')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='content', to='news_app.Type')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='content', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '新闻内容',
                'verbose_name_plural': '新闻内容',
                'db_table': 'news_content',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='评论编号')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('is_deleted', models.BooleanField(default=0, verbose_name='是否删除')),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='news_app.Content', verbose_name='新闻评论')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='评论用户')),
            ],
            options={
                'verbose_name': '新闻评论',
                'verbose_name_plural': '新闻评论',
                'db_table': 'news_comment',
            },
        ),
    ]
