# Generated by Django 3.1.6 on 2021-02-06 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='No Title', max_length=256),
        ),
    ]
