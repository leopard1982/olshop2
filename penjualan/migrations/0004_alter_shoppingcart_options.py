# Generated by Django 4.2.3 on 2023-09-07 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('penjualan', '0003_alter_shoppingcart_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'ordering': ['-id']},
        ),
    ]
