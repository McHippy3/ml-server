# Generated by Django 3.0.2 on 2020-02-20 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_series', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rossmann_sales',
            name='customers',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rossmann_sales',
            name='dayofweek',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rossmann_sales',
            name='open',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rossmann_sales',
            name='promo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rossmann_sales',
            name='schoolholiday',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rossmann_sales',
            name='stateholiday',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rossmann_sales',
            name='store',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]