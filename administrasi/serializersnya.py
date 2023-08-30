from rest_framework import serializers
from administrasi.models import searchKeyword

class serialSearchKeyword(serializers.ModelSerializer):
    class Meta:
        model = searchKeyword
        fields = "__all__"
