# Generated by Django 2.1.7 on 2022-11-04 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='expense',
            table='expense',
        ),
        migrations.AlterModelTable(
            name='income',
            table='income',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]