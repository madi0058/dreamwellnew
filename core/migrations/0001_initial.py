# Generated by Django 4.0.5 on 2022-08-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('channel_id', models.CharField(max_length=255)),
                ('videoCount', models.IntegerField(default=0)),
                ('subscriberCount', models.IntegerField(default=0)),
                ('viewCount', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=255)),
                ('publishedAt', models.DateTimeField()),
                ('thumbnails', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=455)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('publishedAt', models.DateTimeField()),
                ('thumbnails', models.URLField()),
                ('video_id', models.CharField(max_length=255)),
                ('viewCount', models.IntegerField()),
                ('likeCount', models.IntegerField()),
                ('commentCount', models.IntegerField()),
            ],
        ),
    ]
