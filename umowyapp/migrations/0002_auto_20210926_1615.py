# Generated by Django 3.2.7 on 2021-09-26 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('umowyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Powiaty_Wlkp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('powiat', models.CharField(max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rodzaj_umowy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rodz_um', models.CharField(max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rodzaje_jednostek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rodzaj', models.CharField(max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stan_umow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stan', models.CharField(max_length=14, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='umowy',
            name='adres_jedn',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='umowy',
            name='adres_uzyczajacego',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='umowy',
            name='deleted',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='umowy',
            name='informacje',
            field=models.TextField(default='---Niezbędne informacje---'),
        ),
        migrations.AddField(
            model_name='umowy',
            name='kod_pocztowy_jedn',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='umowy',
            name='kod_pocztowy_uzyczajacego',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='umowy',
            name='miasto_jedn',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='umowy',
            name='miasto_uzyczajacego',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='umowy',
            name='nazwa_uzyczajacego',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='umowy',
            name='okres_obowiazywania',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='umowy',
            name='pow_uzyczona',
            field=models.FloatField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='umowy',
            name='rodzaj_kosztow_prad',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='umowy',
            name='skan_umowy',
            field=models.FileField(blank=True, null=True, upload_to='umowy_pdf'),
        ),
        migrations.AlterField(
            model_name='umowy',
            name='nr_umowy',
            field=models.CharField(default='BRAK', max_length=15),
        ),
        migrations.AddField(
            model_name='umowy',
            name='powiaty_jedn',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='umowyapp.powiaty_wlkp'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='umowy',
            name='rodzaj_jedn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='umowyapp.rodzaje_jednostek'),
        ),
        migrations.AddField(
            model_name='umowy',
            name='stan_umowy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='umowyapp.stan_umow'),
        ),
        migrations.AddField(
            model_name='umowy',
            name='typ_umowy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='umowyapp.rodzaj_umowy'),
        ),
    ]