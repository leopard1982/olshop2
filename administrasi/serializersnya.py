from rest_framework import serializers
from administrasi.models import searchKeyword, etalase, kategoriBarang, masterBarang, variasiUkuran
from administrasi.models import variasiVisor, variasiWarna

class serialSearchKeyword(serializers.ModelSerializer):
    class Meta:
        model = searchKeyword
        fields = "__all__"

class serialKategori(serializers.ModelSerializer):
    class Meta:
        model = kategoriBarang
        fields = "__all__"

class serialEtalase(serializers.ModelSerializer):
    class Meta:
        model = etalase
        fields = "__all__"

class serialVariasUkuran(serializers.ModelSerializer):
    class Meta:
        model = variasiUkuran
        fields = "__all__"

class serialVariasVisor(serializers.ModelSerializer):
    class Meta:
        model = variasiVisor
        fields = "__all__"

class serialVariasiWarna(serializers.ModelSerializer):
    class Meta:
        model = variasiWarna
        fields = "__all__"

class serialMasterBarang(serializers.ModelSerializer):
    barang_kategori = serialKategori()
    barang_etalase = serialEtalase()

    class Meta:
        model = masterBarang
        fields = "__all__"