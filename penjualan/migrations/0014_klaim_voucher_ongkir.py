# Generated by Django 4.2.3 on 2023-09-14 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penjualan', '0013_alter_buying_header_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klaim_Voucher_Ongkir',
            fields=[
                ('voucher_kode', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('voucher_min_belanja', models.PositiveBigIntegerField(default=0)),
                ('voucher_terpakai', models.PositiveIntegerField(default=0)),
                ('voucher_valid', models.DateField()),
                ('voucher_klaim', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-voucher_klaim'],
            },
        ),
    ]
