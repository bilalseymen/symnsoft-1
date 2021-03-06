# Generated by Django 4.0 on 2021-12-30 05:17

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('subtitle', models.CharField(max_length=50, null=True)),
                ('content', models.TextField(null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
            ],
        ),
    ]
