from rest_framework import serializers
from penjualan.models import ShoppingCart
from administrasi.models import masterBarang

class serialMasterBarang(serializers.ModelSerializer):
    class Meta:
        model = masterBarang
        fields = "__all__"

class serialShoppingCart(serializers.ModelSerializer):
    shopping_barang = serialMasterBarang()
    class Meta:
        model = ShoppingCart
        fields = "__all__"