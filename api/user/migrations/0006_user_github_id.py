# Generated by Django 3.1.3 on 2021-03-29 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210327_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='github_id',
            field=models.IntegerField(null=True),
        ),
    ]