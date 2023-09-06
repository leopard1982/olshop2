from rest_framework import serializers
from administrasi.models import searchKeyword, merek, kategoriBarang, masterBarang, variasiUkuran
from administrasi.models import variasiVisor, variasiWarna

class serialSearchKeyword(serializers.ModelSerializer):
    class Meta:
        model = searchKeyword
        fields = "__all__"

class serialKategori(serializers.ModelSerializer):
    class Meta:
        model = kategoriBarang
        fields = "__all__"

class serialMerek(serializers.ModelSerializer):
    class Meta:
        model = merek
        fields = "__all__"

class serialVariasUkuran(serializers.ModelSerializer):
    class Meta:
        model = variasiUkuran
        fields = "__all__"

class serialVariasiVisor(serializers.ModelSerializer):
    class Meta:
        model = variasiVisor
        fields = "__all__"

class serialVariasiWarna(serializers.ModelSerializer):
    class Meta:
        model = variasiWarna
        fields = "__all__"

class serialMasterBarang(serializers.ModelSerializer):
    barang_kategori = serialKategori()
    barang_merek = serialMerek()

    class Meta:
        model = masterBarang
        fields = "__all__"