# Generated by Django 4.2.3 on 2023-09-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrasi', '0020_remove_variasiukuran_barang_jumlah_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='alamatRumah',
            fields=[
                ('alamat_nama', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('alamat_detail', models.CharField(default='', max_length=200)),
                ('alamat_propinsi', models.CharField(max_length=200)),
                ('alamat_kota', models.CharField(max_length=200)),
                ('alamat_kecamatan', models.CharField(max_length=200)),
                ('alamat_telpon', models.CharField(max_length=20)),
            ],
        ),
    ]
