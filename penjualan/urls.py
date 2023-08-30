from django.urls import path, re_path, include
from penjualan.views import dashboard, set_search_keyword

urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('api/set/search/',set_search_keyword, name="set_search_keyword")
]
