# Generated by Django 3.2.7 on 2021-11-20 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umowyapp', '0006_umowa_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='umowa',
            old_name='deleted',
            new_name='archiwum',
        ),
    ]
