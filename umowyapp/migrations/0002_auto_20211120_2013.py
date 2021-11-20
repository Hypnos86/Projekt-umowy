# Generated by Django 3.2.7 on 2021-11-20 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umowyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodzaj_umowy',
            name='rodz_um',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='rodzaje_jednostek',
            name='rodzaj',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='stan_umow',
            name='stan',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='umowa',
            name='okres_obowiazywania',
            field=models.DateField(blank=True, null=True),
        ),
    ]
