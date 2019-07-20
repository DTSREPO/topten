# Generated by Django 2.0 on 2019-07-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(default='', max_length=100)),
                ('meta_title', models.CharField(default='', max_length=200)),
                ('meta_description', models.TextField(default='')),
                ('meta_keyword', models.TextField(default='')),
                ('email', models.CharField(default='', max_length=100)),
                ('facebook_url', models.CharField(default='', max_length=300)),
                ('twitter_url', models.CharField(default='', max_length=300)),
                ('google_plus_url', models.CharField(default='', max_length=300)),
                ('youtube_url', models.CharField(default='', max_length=300)),
                ('copyrights', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]