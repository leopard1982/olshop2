from django.db import models
from administrasi.models import masterBarang

# Create your models here.
class ShoppingCart(models.Model):
    shopping_barang = models.ForeignKey(masterBarang, null=False,blank=False,verbose_name="Kode Barang",on_delete=models.RESTRICT)
    shopping_jumlah = models.PositiveIntegerField(default=0)
    shopping_warna = models.CharField(max_length=200, blank=False, null=False)
    shopping_visor = models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
        return self.shopping_barang

    class Meta:
        ordering=['-id']

class WishList_Item(models.Model):
    kode_barang = models.ForeignKey(masterBarang,on_delete=models.RESTRICT,verbose_name="Barang Wishlist")