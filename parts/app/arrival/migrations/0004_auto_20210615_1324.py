# Generated by Django 2.2 on 2021-06-15 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arrival', '0003_auto_20210511_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partsarrival',
            name='partnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partsnumber.PartsNumber', verbose_name='Partsnumber'),
        ),
    ]
