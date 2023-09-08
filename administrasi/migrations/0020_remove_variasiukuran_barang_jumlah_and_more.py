# Generated by Django 4.2.3 on 2023-09-07 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrasi', '0019_alter_masterbarang_barang_merek'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variasiukuran',
            name='barang_jumlah',
        ),
        migrations.RemoveField(
            model_name='variasivisor',
            name='barang_jumlah',
        ),
        migrations.RemoveField(
            model_name='variasiwarna',
            name='barang_jumlah',
        ),
        migrations.AddField(
            model_name='masterbarang',
            name='barang_stok',
            field=models.PositiveIntegerField(default=0),
        ),
    ]