# Generated by Django 4.2.3 on 2023-09-14 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penjualan', '0014_klaim_voucher_ongkir'),
    ]

    operations = [
        migrations.AddField(
            model_name='klaim_voucher_ongkir',
            name='voucher_nilai',
            field=models.PositiveIntegerField(default=0),
        ),
    ]