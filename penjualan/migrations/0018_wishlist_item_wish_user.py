# Generated by Django 4.2.3 on 2023-09-17 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('penjualan', '0017_buying_header_buying_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist_item',
            name='wish_user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]