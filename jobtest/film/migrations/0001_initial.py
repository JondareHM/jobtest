# Generated by Django 3.0 on 2019-12-09 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('poster', models.CharField(max_length=200)),
                ('media', models.CharField(max_length=200)),
            ],
        ),
    ]
