# Generated by Django 3.2.7 on 2021-10-13 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umowyapp', '0005_auto_20211008_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='umowy',
            name='uwagi',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='umowy',
            name='nr_umowy',
            field=models.CharField(default='BRAK', max_length=20, null=True),
        ),
    ]