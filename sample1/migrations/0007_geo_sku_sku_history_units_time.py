# Generated by Django 3.0.2 on 2020-02-02 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample1', '0006_member_master_member_relationship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_code', models.CharField(max_length=54)),
                ('geo_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SKU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku_code', models.CharField(max_length=54)),
                ('sku_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SKU_History_Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_code', models.CharField(max_length=54)),
                ('sku_code', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_code', models.CharField(max_length=54)),
                ('time_description', models.CharField(max_length=255)),
            ],
        ),
    ]
