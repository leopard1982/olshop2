from django.urls import path
from penjualan.views import dashboard, set_search_keyword, get_kategori

urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('api/set/search/',set_search_keyword, name="set_search_keyword"),
    path('api/get/kategori/',get_kategori,name="get_kategori"),
]
