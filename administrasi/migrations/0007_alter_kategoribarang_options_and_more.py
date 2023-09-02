# Generated by Django 4.2.3 on 2023-08-31 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrasi', '0006_remove_kategoribarang_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategoribarang',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='kategoribarang',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='masterbarang',
            name='barang_kategori',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to='administrasi.kategoribarang'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kategoribarang',
            name='barang_kategori',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False, verbose_name='Nama Kategori Barang'),
        ),
        migrations.RemoveField(
            model_name='kategoribarang',
            name='barang_sku',
        ),
    ]