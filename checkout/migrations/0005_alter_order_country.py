# Generated by Django 3.2.20 on 2023-10-02 09:03

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20231001_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=50),
        ),
    ]
