# Generated by Django 4.2.4 on 2023-08-30 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrasi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchkeyword',
            name='keyword',
            field=models.CharField(max_length=50),
        ),
    ]