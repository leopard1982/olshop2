
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('',include('penjualan.urls')),
    path('adm/',include('administrasi.urls')),
    path("admin/", admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, kwargs={'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, kwargs={'document_root': settings.STATICFILES_DIRS}),
]
