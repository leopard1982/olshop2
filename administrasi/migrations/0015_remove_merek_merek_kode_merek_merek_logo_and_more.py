# Generated by Django 4.2.3 on 2023-09-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrasi', '0014_remove_masterbarang_barang_merek'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merek',
            name='merek_kode',
        ),
        migrations.AddField(
            model_name='merek',
            name='merek_logo',
            field=models.ImageField(default='', upload_to='logo_merek'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='merek',
            name='merek_nama',
            field=models.SlugField(default='', primary_key=True, serialize=False),
        ),
    ]