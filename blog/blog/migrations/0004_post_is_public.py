# Generated by Django 3.1.6 on 2021-02-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("blog", "0003_post_author")]

    operations = [
        migrations.AddField(
            model_name="post", name="is_public", field=models.BooleanField(default=True)
        )
    ]
