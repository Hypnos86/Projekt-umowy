# Generated by Django 3.2.7 on 2021-11-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umowyapp', '0004_auto_20211109_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='umowa',
            name='modyfikowany',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
