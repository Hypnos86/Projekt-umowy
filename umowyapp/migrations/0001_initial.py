# Generated by Django 3.2.7 on 2021-09-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Umowy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_umowy', models.DateField(blank=True)),
                ('nr_umowy', models.CharField(max_length=20)),
            ],
        ),
    ]
