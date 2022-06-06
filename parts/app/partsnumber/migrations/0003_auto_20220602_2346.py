# Generated by Django 2.2 on 2022-06-02 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partsnumber', '0002_auto_20210318_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('code', models.CharField(max_length=20, verbose_name='Number Code')),
                ('desc', models.CharField(max_length=200, verbose_name='Soure Code Description')),
            ],
            options={
                'verbose_name': 'Source Code',
                'verbose_name_plural': 'Source Codes',
                'db_table': 'source_code',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='partnumberclass',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='partnumberclass',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='partsnumber',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='partsnumber',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='unitmeasure',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='unitmeasure',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
    ]
