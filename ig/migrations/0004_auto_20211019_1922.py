# Generated by Django 2.2 on 2021-10-19 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ig', '0003_auto_20211019_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Following',
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-comment_posted_on',)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-posted_on']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='like',
            new_name='likes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='count',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pic',
        ),
        migrations.RemoveField(
            model_name='post',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_posted_on',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='description',
            field=models.CharField(null=True, blank=True, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='post_linked',
            field=models.ForeignKey(null=True ,blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ig.Post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, to='ig.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(null=True,blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='biography',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='like',
            name='post_linked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='ig.Post'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
