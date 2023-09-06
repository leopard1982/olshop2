from django.shortcuts import render

from administrasi.serializersnya import serialSearchKeyword, serialKategori, serialMasterBarang
from administrasi.serializersnya import serialVariasiWarna, serialVariasiVisor

from administrasi.models import searchKeyword, kategoriBarang, masterBarang, merek, variasiWarna
from administrasi.models import variasiVisor

from rest_framework.decorators import api_view

from rest_framework.response import Response

from django.db.models import F, Q

from django.core.paginator import Paginator

# Create your views here.
def dashboard(request):
    mereknya = merek.objects.all()
    kategorinya = kategoriBarang.objects.all()
    context = {
        'mereknya':mereknya,
        'kategorinya':kategorinya,
    }
    return render(request,'penjualan/dashboard.html',context)


@api_view(['POST'])
def set_search_keyword(request):
    if request.method == 'POST':
        keywordnya = request.data['keyword']
        if (len(keywordnya)>2):
            if(keywordnya[len(keywordnya) - 1] ==" " and keywordnya[len(keywordnya) -2]==" "):
                pass
            else:
                keywordnya = request.data['keyword'].lower().split(' ')
                jumlah=len(keywordnya)
                
                if(jumlah>1):
                    for keyword in keywordnya[0:jumlah-1]:
                        if keyword!=" ":
                            try:
                                mydata = searchKeyword.objects.get(keyword=keyword)
                                mydata.jumlah = mydata.jumlah+1
                                mydata.save()
                            except:
                                mydata = searchKeyword()
                                mydata.keyword=keyword
                                mydata.jumlah=1
                                mydata.save()

    search_key = searchKeyword.objects.all()[0:4]
    serialnya = serialSearchKeyword(search_key,many=True).data
    context = {
        'keyword': serialnya
    }
    return Response(context)

@api_view(['POST'])
def get_kategori(request):
    if request.method == 'POST':
        kategori = kategoriBarang.objects.all()
        serial = serialKategori(kategori,many=True)
        return Response(serial.data)
    return Response({})


@api_view(['POST'])
def get_barang_cari5(request):
    if request.method == 'POST':
        master = masterBarang.objects.all().order_by('-barang_dicari')[:5]
        serial = serialMasterBarang(master,many=True)
        context = {
            'result':serial.data
        }
        return Response(context)
    return Response({})

@api_view(['POST'])
def cari_keyword(request):
    if request.method == 'POST':
        keyword_cari_stream=request.data['keyword'].strip().split(' ')
        filternya = ""
        q = Q()
        for filter in keyword_cari_stream:
            q = q | Q(barang_nama__icontains=filter)
            print(q)
        data = masterBarang.objects.filter(q)
    
        serial = serialMasterBarang(data,many=True)
        context = {
            'result':serial.data
        }
        return Response(context)
    return Response({})

@api_view(['POST'])
def hasil_cari(request):
    if request.method == 'POST':
        filternya = request.data['kode_sku']
        print(filternya)
        data = masterBarang.objects.get(barang_sku=filternya)
        data.barang_dicari = data.barang_dicari+1
        data.save()
        serial = serialMasterBarang(data)
        context = {
            'result':serial.data
        }
        return Response(context)
    return Response({})

@api_view(['POST'])
def tampil_barang_budget(request):
    if request.method == 'POST':
        q = Q(barang_harga__lt=500000)

        q &= Q(barang_arsip=False)
        mereknya = request.data['merek']
        if mereknya !="":
            q &= Q(barang_merek=merek.objects.get(merek_nama=mereknya))
        kategorinya = request.data['kategori']
        if kategorinya !="":
            q &= Q(barang_kategori=kategoriBarang.objects.get(barang_kategori=kategorinya))   
        harganya = request.data['harga']
        halamannya = int(request.data['halaman'])

        data = masterBarang.objects.all().filter(q)

        if(harganya == "murah"):
            data = data.order_by('barang_harga')
        elif(harganya == "diskon"):
            data = data.order_by('barang_disc')
        elif(harganya=="premium"):
            data = data.order_by('-barang_harga')
        pages = Paginator(data,6)
        page = pages.page(halamannya)
        myresult = []

        
        for p in page:
            myresult.append(p)

        serial = serialMasterBarang(myresult,many=True)
        context = {
            'result': serial.data,
            'max_page': int(pages.num_pages),
        }
        return Response(context)
    return Response({})

@api_view(['POST'])
def tampil_barang_premium(request):
    if request.method == 'POST':
        q = Q(barang_harga__gt=500000)

        q &= Q(barang_arsip=False)

        mereknya = request.data['merek']
        if mereknya !="":
            q &= Q(barang_merek=merek.objects.get(merek_nama=mereknya))
        kategorinya = request.data['kategori']
        if kategorinya !="":
            q &= Q(barang_kategori=kategoriBarang.objects.get(barang_kategori=kategorinya))   
        harganya = request.data['harga']
        halamannya = int(request.data['halaman'])

        data = masterBarang.objects.all().filter(q)

        if(harganya == "murah"):
            data = data.order_by('barang_harga')
        elif(harganya == "diskon"):
            data = data.order_by('barang_disc')
        elif(harganya=="premium"):
            data = data.order_by('-barang_harga')
        pages = Paginator(data,6)
        page = pages.page(halamannya)
        myresult = []

        
        for p in page:
            myresult.append(p)

        serial = serialMasterBarang(myresult,many=True)
        context = {
            'result': serial.data,
            'max_page': int(pages.num_pages),
        }
        return Response(context)
    return Response({})

@api_view(['POST'])
def tampil_barang_disc(request):
    if request.method == 'POST':
        q = Q(barang_disc__gt=0)
        mereknya = request.data['merek']

        q &= Q(barang_disc_aktif=True)

        q &= Q(barang_arsip=False)

        if mereknya !="":
            q &= Q(barang_merek=merek.objects.get(merek_nama=mereknya))
        kategorinya = request.data['kategori']
        if kategorinya !="":
            q &= Q(barang_kategori=kategoriBarang.objects.get(barang_kategori=kategorinya))   
       
        halamannya = int(request.data['halaman'])

        data = masterBarang.objects.all().filter(q).order_by('-barang_disc')

        pages = Paginator(data,6)
        page = pages.page(halamannya)
        myresult = []

        
        for p in page:
            myresult.append(p)

        serial = serialMasterBarang(myresult,many=True)
        context = {
            'result': serial.data,
            'max_page': int(pages.num_pages),
        }
        return Response(context)
    return Response({})

@api_view(['POST'])
def tampil_barang_satu(request):
    if request.method == 'POST':
        kode_barang = request.data['kode_barang']
        data = masterBarang.objects.get(barang_sku=kode_barang)

        serial = serialMasterBarang(data)
        context = {
            'result': serial.data,
        }
        return Response(context)
    return Response({})

@api_view(['POST'])
def variasi_warna(request):
    if request.method == 'POST':
        kode_barang = request.data['kode_barang']
        data = variasiWarna.objects.all().filter(barang_sku=masterBarang.objects.get(barang_sku=kode_barang))

        serial = serialVariasiWarna(data,many=True)
        context = {
            'result': serial.data,
        }
        return Response(context)
    return Response({})

@api_view(['POST'])
def variasi_visor(request):
    if request.method == 'POST':
        kode_barang = request.data['kode_barang']
        data = variasiVisor.objects.all().filter(barang_sku=masterBarang.objects.get(barang_sku=kode_barang))

        serial = serialVariasiVisor(data,many=True)
        context = {
            'result': serial.data,
        }
        return Response(context)
    return Response({})