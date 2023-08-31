from rest_framework import serializers
from administrasi.models import searchKeyword, etalase, kategoriBarang, masterBarang, variasiUkuran, variasiVisor, variasiWarna

class serialSearchKeyword(serializers.ModelSerializer):
    class Meta:
        model = searchKeyword
        fields = "__all__"

class serialKategori(serializers.ModelSerializer):
    class Meta:
        model = kategoriBarang
        fields = "__all__"