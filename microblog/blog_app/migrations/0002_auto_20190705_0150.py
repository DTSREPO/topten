# Generated by Django 2.2.2 on 2019-07-04 19:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='votes',
            field=models.ManyToManyField(blank=True, null=True, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
