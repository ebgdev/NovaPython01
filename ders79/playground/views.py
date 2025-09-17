from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product,Collection,OrderItem, Order,Customer


def say_hello(request):
    # product = Product.objects.all()[0]

    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass

    # product = Product.objects.filter(pk=0).first()

    # --------------

    # to check the existance of an object
    # this will return a boolean value
    # exists = Product.objects.filter(pk=1).exists()
    # return HttpResponse(exists)

    # --------------

    # lets say we want all the products that are 20$
    # queryset = Product.objects.filter(unit_price=20)

    # --------------
    # gt → greater than (>)
    # gte → greater than or equal (>=)
    # lt → less than (<)
    # lte → less than or equal (<=)
    
    # what if we want products that cost more than 20$
    # queryset = Product.objects.filter(unit_price__gt=20)

    # --------------

    # range(20,30)
    # queryset = Product.objects.filter(unit_price__range=(20,30)).order_by('unit_price')
    


    # return render(request, 'hello.html', {
    #     'name': 'ebg',
    #     'products': list(queryset)
    # })

    # --------------

    # find the products that contain coffee in there titles
    # queryset = Product.objects.filter(title__icontains="coffee")

    # --------------

    # products: inventory < 10 and price < 20
    # queryset = Product.objects.filter(inventory__lt=10,unit_price__lt=30)

    # --------------

    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=30)

    # return render(request, 'hello.html', {
    #     'name': 'ebg',
    #     'products': list(queryset),
    # })


    # -------Q objects-------
    # # Django’daki Q objeleri, karmaşık sorgular yazmamızı sağlayan araçlardır.
    # # Normalde filter() kullanırken koşulları AND (&ve) ile zincirleyebiliyoruz. 
    # # Ama bazen OR (|veya), NOT (~değil) gibi daha esnek sorgulara ihtiyaç duyuyoruz.
    # # İşte bu noktada Q devreye giriyor.


    # # products: inventory < 10 OR price < 20
    # # we should use Q objects here
    # # so first from djngo.db.models import Q
    # # each Q object encapsulate (keyword argument)
    # # queryset = Product.objects.filter(Q(inventory__lt =10)|Q(unit_price__lt=30))

    # queryset = Product.objects.filter(Q(inventory__lt =10) | ~Q(unit_price__lt=30))

    # return render(request,'hello.html',{
    #     'name':'ebg',
    #     'products':list(queryset),
    # })



    # -------F objects-------
    # # so first from djngo.db.models import F

    # product = Product.objects.get(id=1)
    # product.inventory += 1
    # product.save()

    # {% if product %}
    # <p> {{product.title}} {{product.inventory}}</p>
    # {% endif %}

    # Bu ne yapıyor?
    # Veritabanından stock çekilir → 10
    # Python’da 10 - 1 = 9 yapılır
    # Geri yazılır
    # Ama ⚠️ aynı anda 2 kişi işlem yaparsa:
    # İkisi de 10 görür
    # İkisi de 9 yazar
    # Sonuç: stok yanlış (aslında 8 olması gerekir).



    # 1 - Race Condition (yarış durumu)
    # Product.objects.filter(id=1).update(inventory=F('inventory') - 1)
    # product = Product.objects.get(id=1)

    # 2
    # fiyat güncelleme : fiyatı %20 arttır
    # Product.objects.update(unit_price=F('unit_price') * 1.2)
    # product = Product.objects.get(id=1)

    # 3
    # Alanlar arası karşılaştırma - ornek henuz yok
    # Product.objects.filter(discounted_price__lt=F('original_price'))

    # return render(request,'hello.html',{
    #     'name':'ebg',
    #     # 'product' : product,
    #     'products' : []
    # })


    # -------Sorting-------

    # ASC
    # queryset = Product.objects.order_by('title')

    # ASC
    # queryset = Product.objects.order_by('-title')

    # Multiple Sorting Items and reverse
    # queryset = Product.objects.order_by('unit_price','title').reverse()


    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')
    # product = Product.objects.latest('unit_price')


    # ------- limiting ---------
    # queryset = Product.objects.all()[:5]
    # queryset = Product.objects.all()[5:10]

    # ---- selecting fields to query ----
    
    # product table has so many fields like id, product_name, slug, product_description, price, image
    # but what if i only want the id and the title ?
    # we get dictionary.
    # queryset = Product.objects.values('id','title')
    # queryset = Product.objects.values('id','title','collection__title')

    # with values_list we get bunch of tuples.
    # queryset = Product.objects.values_list('id','title','collection__title') # bunch of tuples
    # {{ product.collection__title }}
    # ✅ collection__title'a erişebiliyorsun çünkü Product modelinde doğrudan bir ForeignKey ile Collection’a bağlısın.


    # find the products that have been ordered.
    # ✅ 
    queryset = OrderItem.objects.values('product_id','product__title').distinct().order_by("product__title")

    # ‼️ Product Uzerinden
    # ✅ queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title') 

    

    return render(request,'hello.html',{
        'name':'ebg',
        # 'result' : result
        'products' :(queryset),
    })
