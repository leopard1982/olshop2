from django.contrib import admin
from administrasi.models import kategoriBarang, masterBarang, variasiWarna, variasiUkuran, variasiVisor, etalase
# Register your models here.

admin.site.register(masterBarang)
admin.site.register(variasiWarna)
admin.site.register(kategoriBarang)
admin.site.register(variasiVisor)
admin.site.register(variasiUkuran)
admin.site.register(etalase)