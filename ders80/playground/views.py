from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, ExpressionWrapper,DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models.functions import Concat
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from store.models import Product,Collection,OrderItem, Order,Customer
from tags.models import TaggedItem


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


    # queryset = Product.objects.values('title', 'id', 'orderitem__product').distinct().order_by('title')

    # find the products that have been ordered.
    # queryset = OrderItem.objects.values('product_id','product__title').distinct().order_by("product__title")
    # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title') 

    # ---- Deferring Fields ----

    # boylece Model objesine ulasiriz ve bu bazen kotu olabilir , dikkatli olmamiz lazim.
    # (1003 tane sql querisi olusabilir)
    # queryset = Product.objects.only('id','title') # --> id ve title zaten yuklenir ama sonra or: product.slug erismek icin lazy load kullanilir.

    # ---- 
    # bu durumda defer yardimi ile 'description' field'ini erteliyoruz ve description disindakileri yukluyoruz
    # description cagirilmadigi surece asiri yuklenme yasanmaz.
    # template de {{ product.description }} cagirilirsa yaklasik 1003 sql.
    # queryset = Product.objects.defer('description') # yaklasik 3 sql.

    # ---- 13- Selecting Related Objects ----

    # sometimes we need to load bunch of objects together
    # select_related : ForeignKey ve OneToOneField ilişkileri için kullanılır.
    # prefetch_related : ManyToManyField ve reverse ilişkiler için kullanılır.

    # <li>{{ product.collection.title }}</li>
    # queryset = Product.objects.select_related('collection').all()

    # <li> {{ product.title }}</li>
    # queryset = Product.objects.prefetch_related('promotions').all()

    # we also can combines these
    # but in here we dont fill the promotions table yet

    queryset = Product.objects.all().select_related('collection').prefetch_related('promotions')

    return render(request,'hello.html',{
        'name':'ebg',
        # 'product' : product,
        'products' :(queryset),
    })

    # if so :
    # <ul>
    #     {% for product in products %}
    #     <li>
    #         {{ product.title }} -- {{ product.collection.title }} -- 
    #         {% for promo in product.promotions.all %}
    #             {{ promo.description }} ({{ promo.discount }}%) 
    #         {% empty %}
    #             No promotions
    #         {% endfor %}
    #     </li>
    #     {% endfor %}
    # </ul>

# ---------------------------------------------

#     # challenge1: 
#     # Get the last 5 orders with their customer and
#     # items including product

#     queryset = (
#     Order.objects
#     .select_related("customer")                      # fetch customer with order
#     .prefetch_related("orderitem_set__product")      # fetch order items + their products
#     .order_by("-placed_at")[:5]                      # last 5 orders
# )
    

# # <body>
# #   {% if product %}
# #   <p> {{ product }} {{product.title}} {{product.inventory}} ${{ product.unit_price }}</p>
# #   {% endif %}

# #   <ul>
# #   {% for product in products %}
# #     <li>{{product}} - {{ product.id }} -- {{ product.customer.first_name }} -- {{ product.customer.last_name }}</li>
    
# #   {% endfor %}
# #   </ul>
# # </body>




#     return render(request,'hello.html',{
#         'name':'ebg',
#         # 'product' : product,
#         'products' :(queryset),
#     })

# ------------------------------------------------



# ---- Aggregating Objects ----
# from django.db.models.aggregates import Count, Max, Min, Avg, Sum
    # 1️⃣
    # result = Product.objects.aggregate(Count('id'))
    # ornek olarak eger buraya description yazarsak ve description field'inin null olabilecegini varsayarasak
    # null olmayanlarin sayisini bu sekilde ogrenebiliriz

    # we also can change the keyword result: {'id__count': 1000} --> {'count': 1000}
    # 2️⃣
    # result = Product.objects.aggregate(count=Count('id'))

    # 3️⃣
    # result = Product.objects.aggregate(count=Count('id'),min_price=Min('unit_price'))

    # 4️⃣
    # notice that aggregate is one of the queryset methods so we can use something like 
    # check the price with: select * from store_product where collection_id = 3 order by unit_price
    # result = Product.objects.filter(collection__id = 3).aggregate(count=Count('id'),min_price=Min('unit_price'))

    # ---- Annotating Objects ----
    # dipnot koymak
    # Expressions: 
    # 1-Value 
    # 2-F 
    # 3-Func 
    # 4-Aggregate


    # annotate Django ORM’de sorgulara ek sanal alanlar (hesaplanmış değerler) eklemeye yarar.
    # from django.db.models import Value, F
    # check the sql in debug_toolbar

    # 1️⃣
    # queryset = Customer.objects.annotate(new_id = Value(True))
    # NEW_ID --> 1 means True

    # 2️⃣
    # queryset = Customer.objects.annotate(new_id = F('id')+1)

    
    
    # ---- Calling Database Functions ----
    # # from django.db.models import Func

    # queryset = Customer.objects.annotate(
    #     # CONCAT
    #     full_name = Func(F('first_name'),Value(' '),F('last_name'), function='CONCAT')
    # )


    # bu durumda daha kolay yolda var: 
    # from django.db.models.functions import Concat
    # queryset = Customer.objects.annotate(
    #     full_name =  Concat('first_name',Value(' '),'last_name')
    # )

    # ---- Grouping Data ----
    # Now let's see the number of the orders each customer has placed.
    
    
    # number of orders each customer has 
    # in customers class we have reverse relation which gives us --> ❌ order_set
    # building a query (or an annotation, filter, etc.), you use the relationship name (lowercase model name) 
    # rather than the attribute name with _set.
    # Using _set is more about instance attribute access. 
    

    # # this will use left outer join
    # queryset = Customer.objects.annotate(
    #     orders_count = Count('order')
    # )

    # ---- Working with Expression Wrappers ----

    # simdiye kadar Expression'lardan 
    # Value - F - Func - Aggregate Hakkinda konustuk
    # Expression'lardan bir uyge daha sizlere tanitmak istiyorum
    # ✅ ExpressionWrapper (buliding complex expressions)
    # discounted_price = F('unit_price') * 0.8 --> FieldError(‼️ mixed types)
    # unit_price -> decimalField
    # 0.8 -> FloatField

    # ❌
    # queryset = Product.objects.annotate(
    #     discounted_price = F('unit_price') * 0.8
    # )

    # In order to make it work we should first import it and decide what should be the output type
    # from django.db.models import ExpressionWrapper

    # # ✅
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(
    #     discounted_price=discounted_price
    # )

    
    # return render(request, 'hello.html', {
    #     # 'name': 'ebg',
    #     # 'product': product
    #     'products': queryset,
    # })
