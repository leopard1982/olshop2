# Generated by Django 4.2.3 on 2023-09-08 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrasi', '0020_remove_variasiukuran_barang_jumlah_and_more'),
        ('penjualan', '0004_alter_shoppingcart_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_barang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='administrasi.masterbarang', verbose_name='Barang Wishlist')),
            ],
        ),
    ]
