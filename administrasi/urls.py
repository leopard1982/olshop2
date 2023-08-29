from django.urls import path, re_path, include
from administrasi.views import dashboard

urlpatterns = [
    path('',dashboard,name="dashboard"),
]
