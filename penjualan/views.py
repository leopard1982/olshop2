from django.shortcuts import render

from administrasi.serializersnya import serialSearchKeyword, serialKategori, serialMasterBarang

from administrasi.models import searchKeyword, kategoriBarang, masterBarang, etalase

from rest_framework.decorators import api_view

from rest_framework.response import Response

from django.db.models import F, Q

# Create your views here.
def dashboard(request):
    etalasenya = etalase.objects.all()
    return render(request,'penjualan/dashboard.html',{'etalasenya':etalasenya})


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