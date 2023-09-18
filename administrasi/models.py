from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class searchKeyword(models.Model):
    keyword = models.CharField(max_length=50, primary_key=True,null=False,blank=False,default="")
    jumlah = models.IntegerField(default=0)

    class Meta:
        ordering = ['-jumlah']

class merek(models.Model):
    merek_nama = models.SlugField(max_length=50,primary_key=True,blank=False,null=False, default="")
    merek_logo = models.ImageField(upload_to="logo_merek")

    class Meta:
        ordering = ['merek_nama']
    
    def __str__(self):
        return self.merek_nama

class etalase(models.Model):
    etalase_kode = models.CharField(max_length=50, blank=False, null=False, primary_key=True,verbose_name="Kode Etalase", default="")
    etalase_nama = models.CharField(max_length=200, blank=False, null=False, verbose_name="Nama Etalase", default="")

    def __str__(self):
        return self.etalase_nama

class kategoriBarang(models.Model):
    barang_kategori = models.CharField(max_length=50,verbose_name="Nama Kategori Barang",primary_key=True,null=False,blank=False,default="")
    barang_kategori_gambar = models.ImageField(upload_to="kategori_gambar",verbose_name="Gambar Kategori",null=True,blank=True)
    
    def __str__(self):
        return self.barang_kategori

class masterBarang(models.Model):
    barang_sku = models.CharField(max_length=100, primary_key=True, blank=False, null=False, default="",verbose_name="Kode SKU")
    barang_nama = models.CharField(max_length=100, blank=False, null=False, default="", verbose_name="Nama Barang")
    barang_deskripsi = models.TextField(max_length=1000,verbose_name="Deskripsi Barang")
    barang_berat = models.PositiveIntegerField(default=0,null=False,blank=False,verbose_name="Berat Barang dalam Gram")
    barang_foto1 = models.ImageField(upload_to='barang',verbose_name="Gambar Barang #1",null=True,blank=True)
    barang_foto2 = models.ImageField(upload_to='barang',verbose_name="Gambar Barang #2",null=True,blank=True)
    barang_foto3 = models.ImageField(upload_to='barang',verbose_name="Gambar Barang #3",null=True,blank=True)
    barang_foto4 = models.ImageField(upload_to='barang',verbose_name="Gambar Barang #4",null=True,blank=True)
    barang_foto5 = models.ImageField(upload_to='barang',verbose_name="Gambar Barang #5",null=True,blank=True)
    barang_foto6 = models.ImageField(upload_to='barang',verbose_name="Gambar Barang #6",null=True,blank=True)
    barang_harga = models.PositiveBigIntegerField(default=0,verbose_name="Harga Barang (Rupiah)")
    barang_arsip = models.BooleanField(default=False,verbose_name="Barang Diarsipkan? (arsip->tidak ditampilkan)")
    barang_new = models.BooleanField(default=True,verbose_name="Barang di set NEW?")
    barang_disc = models.PositiveSmallIntegerField(default=0,verbose_name="Discount Harga Barang (Rupiah)")
    barang_disc_aktif = models.BooleanField(default=False,verbose_name="Discount diaktifkan?")
    barang_ongkir = models.PositiveIntegerField(default=0,verbose_name="Gratis Ongkir Barang (Rupiah)")
    barang_ongkir_aktif = models.BooleanField(default=False,verbose_name="Gratis Ongkir diaktifkan?")
    barang_kategori = models.ForeignKey(kategoriBarang,on_delete=models.RESTRICT,verbose_name="Kategori Barang")
    barang_terjual = models.PositiveIntegerField(default=0,verbose_name="Barang Jumlah Terjual")
    barang_dicari = models.PositiveIntegerField(default=0,verbose_name="Jumlah HIT")
    barang_merek = models.ForeignKey(merek,on_delete=models.RESTRICT,null=True,blank=True)
    barang_stok = models.PositiveIntegerField(default=0)


    class Meta:
        ordering = ['barang_nama','barang_sku']
        unique_together = ['barang_nama','barang_sku']

    def __str__(self):
        return self.barang_nama
    
class variasiWarna(models.Model):
    barang_sku = models.ForeignKey(masterBarang,on_delete=models.RESTRICT,verbose_name="Nama Barang")
    barang_warna = models.CharField(max_length=50,verbose_name="Nama Variasi Warna")

    class Meta:
        ordering = ['barang_sku','barang_warna']
        unique_together = ['barang_sku','barang_warna']
    
    def __str__(self):
        return str(self.barang_sku) + "/" +self.barang_warna

class variasiVisor(models.Model):
    barang_sku = models.ForeignKey(masterBarang,on_delete=models.RESTRICT,verbose_name="Jenis Visor Barang")
    barang_visor = models.CharField(max_length=50,verbose_name="Nama Variasi Visor")
    barang_visor_gambar = models.ImageField(upload_to="visor", verbose_name="Gambar Visor",null=True,blank=True)

    class Meta:
        ordering = ['barang_sku','barang_visor']
        unique_together = ['barang_sku','barang_visor']
    
    def __str__(self):
        return str(self.barang_sku) + "/" +self.barang_visor

class variasiUkuran(models.Model):
    barang_sku = models.ForeignKey(masterBarang,on_delete=models.RESTRICT,verbose_name="Ukuran Barang")
    barang_ukuran = models.CharField(max_length=50,verbose_name="Nama Variasi Ukuran")

    class Meta:
        ordering = ['barang_sku','barang_ukuran']
        unique_together = ['barang_sku','barang_ukuran']
    
    def __str__(self):
        return str(self.barang_sku) + "/" + self.barang_ukuran

class chatHeader(models.Model):
    chat_id = models.CharField(max_length=100,primary_key=True,null=False,blank=False) #chat_id = username-kodebarang
    chat_user = models.ForeignKey(User, on_delete=models.RESTRICT)

class chatBody(models.Model):
    chat_id = models.ForeignKey(chatHeader,on_delete=models.RESTRICT)
    chat_message = models.TextField(max_length=500,blank=False,null=False)
    chat_time = models.DateTimeField(auto_now_add=True)
    chat_user = models.ForeignKey(User,on_delete=models.RESTRICT)

class alamatRumah(models.Model):
    alamat_nama = models.CharField(max_length=100,default="",primary_key=True,null=False,blank=False)
    alamat_detail = models.CharField(max_length=200,default="")
    alamat_propinsi = models.CharField(max_length=200)
    alamat_kota = models.CharField(max_length=200)
    alamat_kecamatan = models.CharField(max_length=200)
    alamat_telpon = models.CharField(max_length=20)

class emailKonfirm(models.Model):
    email = models.EmailField(max_length=200, blank=False,null=False,primary_key=True)
    kode = models.CharField(max_length=8)
    exp = models.DateTimeField()

    