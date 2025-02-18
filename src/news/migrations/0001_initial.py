# Generated by Django 5.0.2 on 2025-02-09 14:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('content', models.TextField(verbose_name='内容')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時')),
                ('published_at', models.DateTimeField(blank=True, null=True, verbose_name='公開日時')),
                ('is_published', models.BooleanField(default=False, verbose_name='公開する')),
            ],
            options={
                'verbose_name': 'ニュース記事',
                'verbose_name_plural': 'ニュース記事',
                'ordering': ['-created_at'],
            },
        ),
    ]
