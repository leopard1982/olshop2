from django.db import models
from administrasi.models import masterBarang

# Create your models here.
class ShoppingCart(models.Model):
    shopping_barang = models.ForeignKey(masterBarang, null=False,blank=False,verbose_name="Kode Barang",on_delete=models.RESTRICT)
    shopping_jumlah = models.PositiveIntegerField(default=0)
    shopping_warna = models.CharField(max_length=200, blank=False, null=False)
    shopping_visor = models.CharField(max_length=200,blank=False,null=False)