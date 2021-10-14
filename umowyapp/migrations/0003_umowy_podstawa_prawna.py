# Generated by Django 3.2.8 on 2021-10-14 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('umowyapp', '0002_remove_umowy_podstawa_prawna'),
    ]

    operations = [
        migrations.AddField(
            model_name='umowy',
            name='podstawa_prawna',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='umowyapp.podstawa_prawna'),
        ),
    ]