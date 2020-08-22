# Generated by Django 3.0.8 on 2020-08-22 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='cover',
            field=models.ImageField(null=True, upload_to='covers/'),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile_pic/'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('content_text', models.CharField(max_length=140)),
                ('content_image', models.ImageField(null=True, upload_to='posts/')),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField(max_length=90)),
                ('comment_time', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenters', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='network.Post')),
            ],
        ),
    ]
