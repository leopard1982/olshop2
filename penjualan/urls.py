from django.urls import path
from penjualan.views import dashboard, set_search_keyword, get_kategori, get_barang_cari5
from penjualan.views import cari_keyword, hasil_cari, tampil_barang_budget, tampil_barang_premium
from penjualan.views import tampil_barang_disc, tampil_barang_satu, variasi_warna, variasi_visor
from penjualan.views import addCart, get_cart, addJumlahCart, subJumlahCart, setWishlist, initialWishlist
from penjualan.views import getWishlist, hapusCart, proses_bayar, update_notif_bayar

urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('api/set/search/',set_search_keyword, name="set_search_keyword"),
    path('api/get/search/',cari_keyword, name="cari_keyword"),
    path('api/get/search/hasil/',hasil_cari, name="hasil_cari"),
    path('api/get/kategori/',get_kategori,name="get_kategori"),
    path('api/get/barang/cari5/',get_barang_cari5,name="get_barang_cari5"),
    path('api/get/barang/budget/',tampil_barang_budget,name="tampil_barang_budget"),
    path('api/get/barang/premium/',tampil_barang_premium,name="tampil_barang_premium"),
    path('api/get/barang/discount/',tampil_barang_disc,name="tampil_barang_disc"),
    path('api/get/barang/satu/',tampil_barang_satu,name="tampil_barang_satu"),
    path('api/get/barang/warna/',variasi_warna,name="warna_warna"),
    path('api/get/barang/visor/',variasi_visor,name="warna_visor"),
    path('api/add/cart/',addCart,name="add_cart"),
    path('api/get/cart/',get_cart,name="get_cart"),
    path('api/set/cart/kurangi/',subJumlahCart,name="subJumlahCart"),
    path('api/set/cart/tambahi/',addJumlahCart,name="addJumlahCart"),
    path('api/set/wishlist/',setWishlist,name="setWishlist"),
    path('api/init/wishlist/',initialWishlist,name="initialWishlist"),
    path('api/get/wishlist/',getWishlist,name="getWishList"),
    path('api/del/cart/',hapusCart,name="hapusCart"),
    path('api/set/bayar/',proses_bayar,name='proses_bayar'),
    path('api/get/bayar/',update_notif_bayar,name='update_notif_bayar'),
]
