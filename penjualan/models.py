from django.db import models
from administrasi.models import masterBarang
from django.contrib.auth.models import User

# Create your models here.
class ShoppingCart(models.Model):
    shopping_user = models.ForeignKey(User,on_delete=models.RESTRICT)
    shopping_barang = models.ForeignKey(masterBarang, null=False,blank=False,verbose_name="Kode Barang",on_delete=models.RESTRICT)
    shopping_jumlah = models.PositiveIntegerField(default=0)
    shopping_warna = models.CharField(max_length=200, blank=False, null=False)
    shopping_visor = models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
        return self.shopping_barang

    class Meta:
        ordering=['-id']

class WishList_Item(models.Model):
    wish_user = models.ForeignKey(User,on_delete=models.RESTRICT)
    kode_barang = models.ForeignKey(masterBarang,on_delete=models.RESTRICT,verbose_name="Barang Wishlist")

class Voucher_Ongkir(models.Model):
    voucher_kode = models.CharField(max_length=200,primary_key=True,null=False,blank=False)
    voucher_nama = models.CharField(max_length=200)
    voucher_valid = models.DateField(auto_now_add=False)
    voucher_min_belanja = models.PositiveBigIntegerField(default=0)
    voucher_nilai = models.PositiveIntegerField(default=0)
    voucher_aktif = models.BooleanField(default=True)
    voucher_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-voucher_time']

    def __str__(self):
        return self.voucher_nama
    
class Klaim_Voucher_Ongkir(models.Model):
    voucher_user = models.ForeignKey(User,on_delete=models.RESTRICT)
    voucher_kode = models.CharField(max_length=200,primary_key=True,null=False,blank=False)
    voucher_min_belanja = models.PositiveBigIntegerField(default=0)
    voucher_terpakai = models.PositiveIntegerField(default=0)
    voucher_valid = models.DateField(auto_now_add=False)
    voucher_klaim = models.DateTimeField(auto_now_add=True)
    voucher_nilai = models.PositiveIntegerField(default=0)
    voucher_nama = models.CharField(max_length=200)

    class Meta:
        ordering = ['-voucher_klaim']

    def __str__(self):
        return self.voucher_kode

class Buying_Header(models.Model):
    buying_user = models.ForeignKey(User,on_delete=models.RESTRICT)
    buying_kode = models.CharField(max_length=10, blank=False, null=False,primary_key=True)
    buying_total = models.PositiveBigIntegerField(null=True,blank=True,default=0)
    buying_kirim_resi = models.CharField(max_length=200, blank=True,null=True)
    buying_kirim_ekspedisi = models.CharField(max_length=200, blank=True, null=True)
    buying_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-buying_time"]

class Buying_Detail(models.Model):
    buying_kode = models.ForeignKey(Buying_Header,on_delete=models.RESTRICT)
    buying_barang = models.ForeignKey(masterBarang, null=False,blank=False,verbose_name="Kode Barang",on_delete=models.RESTRICT)
    buying_jumlah = models.PositiveIntegerField(default=0)
    buying_warna = models.CharField(max_length=200, blank=False, null=False)
    buying_visor = models.CharField(max_length=200,blank=False,null=False)
    buying_pesan = models.CharField(max_length=200,blank=False,null=False)