# Generated by Django 2.2.19 on 2021-04-05 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
