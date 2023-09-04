from django.urls import path
from penjualan.views import dashboard, set_search_keyword, get_kategori, get_barang_cari5
from penjualan.views import cari_keyword, hasil_cari, tampil_barang_budget
urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('api/set/search/',set_search_keyword, name="set_search_keyword"),
    path('api/get/search/',cari_keyword, name="cari_keyword"),
    path('api/get/search/hasil/',hasil_cari, name="hasil_cari"),
    path('api/get/kategori/',get_kategori,name="get_kategori"),
    path('api/get/barang/cari5/',get_barang_cari5,name="get_barang_cari5"),
    path('api/get/barang/budget/',tampil_barang_budget,name="tampil_barang_budget"),
]
