# Generated by Django 2.2.7 on 2019-11-17 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0003_userconnection'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
