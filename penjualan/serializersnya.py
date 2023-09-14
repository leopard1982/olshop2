from rest_framework import serializers
from penjualan.models import ShoppingCart, WishList_Item, Buying_Detail, Buying_Header, Voucher_Ongkir
from penjualan.models import Klaim_Voucher_Ongkir
from administrasi.models import masterBarang, alamatRumah

class serialMasterBarang(serializers.ModelSerializer):
    class Meta:
        model = masterBarang
        fields = "__all__"

class serialShoppingCart(serializers.ModelSerializer):
    shopping_barang = serialMasterBarang()
    class Meta:
        model = ShoppingCart
        fields = "__all__"

class serialWishList(serializers.ModelSerializer):
    kode_barang = serialMasterBarang()
    class Meta:
        model = WishList_Item
        fields = "__all__"

class serialBuyingHeader(serializers.ModelSerializer):
    class Meta:
        model = Buying_Header
        fields = "__all__"

class serialBuyingDetail(serializers.ModelSerializer):
    buying_kode = serialBuyingHeader()
    class Meta:
        model = Buying_Detail
        fields = "__all__"

class serialGratisOngkir(serializers.ModelSerializer):
    class Meta:
        model = Voucher_Ongkir
        fields = "__all__"

class serialKlaimGratisOngkir(serializers.ModelSerializer):
    class Meta:
        model = Klaim_Voucher_Ongkir
        fields = "__all__"

class serialAlamatRumah(serializers.ModelSerializer):
    class Meta:
        model = alamatRumah
        fields = "__all__"