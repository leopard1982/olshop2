from django.shortcuts import render

from random import random

from administrasi.serializersnya import serialSearchKeyword, serialKategori, serialMasterBarang
from administrasi.serializersnya import serialVariasiWarna, serialVariasiVisor

from administrasi.models import searchKeyword, kategoriBarang, masterBarang, merek, variasiWarna
from administrasi.models import variasiVisor, alamatRumah, emailKonfirm

from penjualan.serializersnya import serialShoppingCart, serialWishList, serialKlaimGratisOngkir
from penjualan.serializersnya import serialBuyingDetail, serialBuyingHeader, serialGratisOngkir
from penjualan.serializersnya import serialAlamatRumah

from penjualan.models import ShoppingCart, WishList_Item, Buying_Header, Buying_Detail
from penjualan.models import Voucher_Ongkir, Klaim_Voucher_Ongkir

from rest_framework.decorators import api_view

from rest_framework.response import Response

from datetime import datetime,timedelta

from django.db.models import F, Q

from django.core.paginator import Paginator

from django.core.mail import send_mail

from django.conf import settings

import json

import os


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

@api_view(['POST'])
def addCart(request):
    if request.method == 'POST':
        kode_barang = request.data['kode_barang']
        jumlah_barang = request.data['jumlah_barang']
        warna_barang = request.data['warna_barang']
        visor_barang = request.data['visor_barang']

        id_cart = None

        data = ShoppingCart.objects.all().filter(shopping_barang=masterBarang.objects.get(barang_sku=kode_barang),shopping_warna=warna_barang,shopping_visor=visor_barang)
        if(data.count()>0):
            data.update(shopping_jumlah = F('shopping_jumlah')+jumlah_barang)
            id_cart = data[0].id
        else:
            data = ShoppingCart()
            data.shopping_barang = masterBarang.objects.get(barang_sku=kode_barang)
            data.shopping_jumlah = jumlah_barang
            data.shopping_visor = visor_barang
            data.shopping_warna = warna_barang
            data.save()
            id_cart = ShoppingCart.objects.all().order_by("-id")[0].id

            context = {
                'id_cart':id_cart,
                'result': True
            }
            print(context)
            return Response (context)
    return Response ({'result':False})

@api_view(['POST'])
def get_cart (request):
    if request.method == 'POST':
        mydata = ShoppingCart.objects.all()
        serial = serialShoppingCart(mydata,many=True)

        context= {
            'result': serial.data,
            'jumlah_item': mydata.count()
        }

        return Response(context)
    return Response({})

@api_view(['POST'])
def get_cart_id (request):
    if request.method == 'POST':
        
            visor = request.data['visor']
            warna = request.data['warna']
            kode_barang = request.data['kode_barang']
            try:
                mydata = ShoppingCart.objects.all().get(shopping_visor=visor, shopping_warna=warna, shopping_barang = masterBarang.objects.get(barang_sku=kode_barang)).id
            except:
                mydata = ShoppingCart.objects.all()[0].id
            context= {
                'id_cart': mydata,
                'result':True
            }

            return Response(context)
    
    return Response({})

@api_view(['POST'])
def addJumlahCart (request):
    if request.method == 'POST':
        idnya = request.data['id']
       
        # kode_barang = request.data['kode_barang']
        # variasi_visor = request.data['variasi_visor']
        # variasi_warna = request.data['variasi_warna']
        mydata = ShoppingCart.objects.get(id=idnya)
        if mydata is not None:
            mydata.shopping_jumlah=mydata.shopping_jumlah+1
            mydata.save()
        context= {
            'result':True
        }

        return Response(context)
    return Response({'result':False})

@api_view(['POST'])
def subJumlahCart (request):
    if request.method == 'POST':
        idnya = request.data['id']
        
        # kode_barang = request.data['kode_barang']
        # variasi_visor = request.data['variasi_visor']
        # variasi_warna = request.data['variasi_warna']
        
        mydata = ShoppingCart.objects.get(id=idnya)
        if mydata is not None:
    
            if(mydata.shopping_jumlah==1):
                mydata.delete()
            else:
                mydata.shopping_jumlah = mydata.shopping_jumlah -1
                mydata.save()

        context= {
            'result':True
        }

        return Response(context)
    return Response({'result':False})

@api_view(['POST'])
def setWishlist (request):
    jumlah=0
    if request.method == 'POST':
        kode_barang = request.data['kode_barang']
        print(kode_barang)
        try:
            mydata = WishList_Item.objects.get(kode_barang=masterBarang.objects.get(barang_sku=kode_barang))       
            mydata.delete()
            resultnya=False
        except:       
            mydata1=WishList_Item()
            mydata1.kode_barang = masterBarang.objects.get(barang_sku=kode_barang)
            mydata1.save()
            
            resultnya=True
        print(kode_barang)

        data = WishList_Item.objects.all()
        jumlah = data.count()
        serial = serialWishList(data,many=True)

        context = {
            'result': resultnya,
            'jumlah':jumlah,
            'data': serial.data
        }
        return Response(context)
    return Response({})

@api_view(['POST'])
def getWishlist (request):
    resultnya = False
    jumlah=0
    if request.method == 'POST':
        kode_barang = request.data['kode_barang']

        mydata = WishList_Item.objects.all().filter(kode_barang=masterBarang.objects.get(barang_sku=kode_barang))       
        if mydata.count()>0:
           resultnya = True

        context = {
            'result': resultnya,

        }
        return Response(context)
    return Response({})

@api_view(['POST'])
def initialWishlist (request):
    if request.method == 'POST':
        mydata = WishList_Item.objects.all()       
        
        resultnya=True

        data = WishList_Item.objects.all()
        jumlah = data.count()
        serial = serialWishList(data,many=True)

        context = {
            'result': resultnya,
            'jumlah': jumlah,
            'data': serial.data
        }
        return Response(context)
    return Response({})

@api_view(['POST'])
def hapusCart(request):
    if request.method == 'POST':
        id_cart = request.data['id_cart']
        ShoppingCart.objects.all().filter(id=id_cart).delete()
        return Response({'result':True})
    return Response({})

@api_view(['POST'])
def proses_bayar(request):
    filternya = Q()

    data=None

    random_id = ""
    for i in range(0,20):
        random_id = random_id + str(int(random()*10))
    
    if request.method == 'POST':
        list_json = json.loads(request.data['dibayar'])
        total_harga = 0
        total_item=0
        #buat headernya dulu
        buy_header = Buying_Header()
        buy_header.buying_kode=random_id
        buy_header.save()
        
        for list in list_json:
            cart_id = list['id']
            pesan = list['request']
            data = ShoppingCart.objects.get(id=int(cart_id))
            harga = data.shopping_barang.barang_harga
            if data.shopping_barang.barang_disc_aktif==True:
                harga = harga - data.shopping_barang.barang_disc
            total_harga = total_harga + harga * data.shopping_jumlah

            total_item = total_item+1
            
            #tambahkan detail buyingnya
            buy_detail = Buying_Detail()
            buy_detail.buying_kode = Buying_Header.objects.get(buying_kode=random_id)
            buy_detail.buying_barang = data.shopping_barang
            buy_detail.buying_jumlah = data.shopping_jumlah
            buy_detail.buying_visor = data.shopping_visor
            buy_detail.buying_warna = data.shopping_warna
            buy_detail.buying_pesan = pesan
            buy_detail.save()

        #email konfirmasi
        send_mail("Konfirmasi Belanja #" + str(random_id),"Terima kasih untuk pembelanjaanmu dengan nomor transaksi: " + str(random_id),"Email Konfirmasi <adhy.chandra@live.co.uk>",["yulian.cute@gmail.com"])            

        Buying_Header.objects.all().filter(buying_kode=random_id).update(buying_total=total_harga)

        return Response({'result':True})
    return Response({'result':False})


@api_view(['POST'])
def update_notif_bayar(request):
    if request.method=="POST":
        data = Buying_Detail.objects.all()
        serial = serialBuyingDetail(data,many=True)
        jumlah_blm_bayar = Buying_Header.objects.all().count()
        data2 = Buying_Header.objects.all().order_by("-buying_time")
        serial2 = serialBuyingHeader(data2,many=True)
        context = {
            'result': True,
            'pembayaran_detail':serial.data,
            'pembayaran_header':serial2.data,
            'jumlah_blm_bayar':jumlah_blm_bayar,
        }
        return Response(context)
    
    return Response({'result':False})

@api_view(['POST'])
def get_voucher_ongkir(request):
    if request.method=="POST":
        data = Voucher_Ongkir.objects.all().filter(Q(voucher_valid__gte=datetime.today()) & Q(voucher_aktif=True))
        serial = serialGratisOngkir(data,many=True)
        context = {
            'result': True,
            'data': serial.data
        }
        return Response(context)
    
    return Response({'result':False})


@api_view(['POST'])
def klaim_voucher_ongkir(request):
    if request.method=="POST":
        kode_voucher = request.data['kode_voucher']
        nilai = request.data['nilai']
        min_belanja = request.data['min_belanja']
        valid = request.data['valid']
        tahun = int(valid.split('-')[0])
        bulan = int(valid.split('-')[1])
        hari = int(valid.split('-')[2])
        valid=datetime(tahun,bulan,hari)
        nama_voucher = request.data['nama_voucher']
         
        claim = Klaim_Voucher_Ongkir.objects.all().filter(voucher_kode=kode_voucher)
        if (claim.count() > 0) :
            return Response({'result':False})
        else:
            claim = Klaim_Voucher_Ongkir()
            claim.voucher_kode = kode_voucher
            claim.voucher_nilai = nilai
            claim.voucher_min_belanja = min_belanja
            claim.voucher_valid = valid
            claim.voucher_terpakai=False
            claim.voucher_nama=nama_voucher
            claim.save()
            return Response({'result':True})
    return Response({'result':False})

@api_view(['POST'])
def get_klaim_voucher_ongkir(request):
    if request.method=="POST":     
        data = Klaim_Voucher_Ongkir.objects.all().filter(voucher_terpakai=False,voucher_valid__gte=datetime.today())
        serial = serialKlaimGratisOngkir(data,many=True)
        jumlah = data.count()
        context = {
            'result':True,
            'data':serial.data,
            'jumlah':jumlah
        }
        return Response(context)
    return Response({'result':False})

@api_view(['POST'])
def get_alamat_rumah(request):
    if request.method == 'POST':
        data = alamatRumah.objects.all()
        serial = serialAlamatRumah(data,many=True)

        context={
            'data':serial.data
        }

        return Response(context)
    return Response({})

@api_view(['POST'])
def createKode(request):
    kode=""
    if request.method=="POST":
        email = request.data['email']
        data = emailKonfirm.objects.all().filter(email=email)
        
        for x in range(0,10):
            kode = kode + str(int(random()*10))
        if(data.count()>0):
            data.update(kode=kode,exp = datetime.today() + timedelta(minutes=5))
        else:
            data = emailKonfirm()
            data.email = email
            data.kode = kode
            data.exp = datetime.now() + timedelta(minutes=5)
            data.save()
        try:
            send_mail("Kode Konfirmasi","jagoanhelm.com - kode rahasia anda adalah: \n\n%s\n\nSilakan konfirmasi dalam 5 menit."%kode,"adhy.chandra@live.co.uk",[email])
            return Response({'result':True})
        except:
            return Response({'result':False})
    return Response({'result':False})

@api_view(['POST'])
def getKode(request):
    kode=""
    
    if request.method=="POST":
        print(request.data)
        email = request.data['email']
        kode = request.data['kode']
        data = emailKonfirm.objects.all().filter(email=email,kode=kode,exp__gte=datetime.now())
        print(data)
        if(data.count()>0):
            data.delete()
            return Response({'result':True})
    
    return Response({'result':False})