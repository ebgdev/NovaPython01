from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, ExpressionWrapper,DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models.functions import Concat
from django.db import transaction,connection 
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

    # ---- Selecting Related Objects ----

    # sometimes we need to load bunch of objects together
    # select_related : ForeignKey ve OneToOneField ilişkileri için kullanılır.
    # prefetch_related : ManyToManyField ve reverse ilişkiler için kullanılır.

    # <li>{{ product.collection.title }}</li>
    # queryset = Product.objects.select_related('collection').all()

    # <li> {{ product.title }}</li>
    # queryset = Product.objects.prefetch_related('promotions').all()

    # we also can combines these
    # but in here we dont fill the promotions table yet

    # queryset = Product.objects.all().select_related('collection').prefetch_related('promotions')

    # return render(request,'hello.html',{
    #     'name':'ebg',
    #     # 'product' : product,
    #     'products' :(queryset),
    # })

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

# #   <ul>C
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

    
    
    # ---- alling Database Functions ----
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

    
    
    # # ---- Querying Generic Relationships ----
    # # we do create a class TaggedItem which type's is ContentType(Generic)


    # # DataGrip --> django_content_type table (all the models that we have in our model)
    # # in the admin app we have logentry (comes with django)
    # # ...

    # # Let's now look at tags_taggeditem
    # # object_id , content_type_id , tag_id

    # # content_type_id
    # # xxx(mine is 12)  |  store  |  product

    # # Notice: what are we looking for is 
    # # we should write a query to filter all records where content_type_id = 12
    # # object_id is equal to product_id 


    # # lets first import few classes
    # # from django.contrib.contenttypes.models import ContentType
    # # from store.models import Product
    # # from tags.models import TaggedItem

    # # contenttype manager object has a special method : get_for_model
    # content_type = ContentType.objects.get_for_model(Product) # --> 12


    # # preload the tag field
    # queryset = TaggedItem.objects.select_related('tag').filter(

    #     # Give me all TaggedItem rows where the tag is attached to a Product model.
    #     content_type = content_type, # (12)

    #     # this will happen dynamically later 
    #     # (we are going to get product from URL that customer is looking for)
    #     # and the pass it here.
    #     object_id = 1 # (product with the ID=1)
    # )



    # return render(request, 'hello.html', {
    #     # 'name': 'ebg',
    #     # 'product':
    #     'products': queryset,
    # })

    
    
    
    # ---- Custom Managers ----

    # # Her defasinda ilgili content_type modelini bulmak 
    # # Sonra olnlarin icinden sadece 'tag' cekmek ve ...
    # # soyle bir yapsak cok iyi olmaz mi ? TaggedItem.objects.get_tags_for(Product,1)

    # # bunu yapabilmek icin varsayilan object managerimizi degistirmemiz gerekecek
    # # 1.tags>models.py 'da custome manager yazmak.
    
    # # 2. class TaggedItem 'da
    
    # # class TaggedItem(models.Model):
    # #   objects = TaggedItemManager()
    # #   ...
    

    # queryset = TaggedItem.objects.get_tags_for(Product,1)


    # return render(request, 'hello.html', {
    #     # 'name': 'ebg',
    #     # 'product':
    #     'products': queryset,
    # })
    


# ---- Understanding QuerySet Cache ----

    # # biliyoruz ki verileri disk'ten okumak memory'den okumak'tan kat kat yavas.
    # # bu yuzden django kendisi bir optimizasyon teknigi olan queryset cache kullanir.
    # # simdi

    # # 1️⃣ o yuzden bu kodda ben 2 kez list(queryset) dedigme ragmen sadece 1 ilk defa query gonderilir
    # # queryset = Product.objects.all()
    # # list(queryset)
    # # list(queryset)

    # # cunku 2.kez icin veriler artik memory de cache de tutuluyor
    
    # # 2️⃣ ayni sekilde eger queryset[0] cagirirsam cache'den veriyi cekebiliriz
        
    # # queryset = Product.objects.all()
    # # list(queryset)
    # # list(queryset)
    # # queryset[0]

    # # 3️⃣ ama eger once queryset[0] cekip ardindan list(queryset)
    # # dersek 2 query gonderilir:
    
    # queryset = Product.objects.all()
    # queryset[0]
    # list(queryset)




    # return render(request, 'hello.html', {
    #     # 'name': 'ebg',
    #     # 'product':
    #     'products': queryset,
    # })



# ---- Creating Objects ----

# # the other approaches that I comment them out are not preferred
# # most of the time they dont get renamed automatically or event dosen't support auto completion

#     collection = Collection()
#     # collection = Collection(title ='Video Games')
#     # Even though the code is shorter but if in the feature 
#     # we decide to rename the title to another thing , field wont get updated.
#     collection.title = 'Video Games'
#     collection.featured_product = Product(pk=1)
#     # collection.featured_product_id = 1

#     # to insert this data to the collection table we should use save() method.
#     collection.save()


#     # Instead of these 4 lines we also can use create (❌ Not preferred)
#     # collection = Collection.objects.create(title='Video Games',featured_product_id=1)


#     return render(request,'hello.html')

#     # if you want to revert the database:

#     # delete from store_collection
#     # where id = 13;



# ---- Updating Objects ----

# In order to update a table we should pass the ✅pk/❌id to the Collection
# otherwise it will work like insert mode
    
    # collection = Collection(pk=12)
    # collection.title = 'Video Games'
    # collection.featured_product = None
    # collection.save()


# But what if we only want to update only title

    # collection = Collection(pk=12)
    # # ❌
    # collection.title = 'Games'
    # collection.save()

# ‼️ Data Loss
# what will happen now django will set collection.featured_product to an empty string.

# So in order to update properly we should first fetch the values from the database
# so we have all the values in our memory , then we can update the field

    # 1️⃣ get + save
    # collection = Collection.objects.get(pk=12)
    # collection.title = 'Games'
    # collection.save()

    # # 2️⃣ filter + update
    Collection.objects.filter(pk=12).update(title='Video Games')

    return render(request,'hello.html')



# ---- Deleting Objects ----

    # # Single:
    # # collection = Collection(pk=12)
    # # collection.delete()

    # # Multiple:
    # Collection.objects.filter(pk__gt=11).delete()


    # # Other Examples:
    # # Collection.objects.filter(Q(pk=6) | Q(pk=10)).delete()
    # # Collection.objects.filter(pk__in=[6, 10]).delete()

    # return render(request,'hello.html')


# ---- Transactions ----

# # Bazen veritabanımıza birden fazla değişikliği aynı anda uygulamak isteriz 
# # ve olası bir hata durumunda hiçbir şeyin kaydedilmemesini isteriz. 
# # Yani ya başarılı olur ve her şey kaydedilir 
# # ya da başarısız olur ve hiçbir değişiklik yapılmaz.

# # from django.db import transaction

# # 1️⃣
# # @transaction.atomic()
# #def say_hello(request):

# # # ornegin odemeler ve siparisler

# #     # first parent record
# #     order = Order()
# #     order.customer_id = 1
# #     order.save()

# #     # child record
# #     item = OrderItem()
# #     item.order = order
# #     item.product_id = 1
# #     item.quantity = 1
# #     item.unit_price = 10
# #     item.save()


# # 2️⃣
#     with transaction.atomic():
#         order = Order()
#         order.customer_id = 1
#         order.save()

#         item = OrderItem()
#         item.order = order
#         item.product_id = 1 # change it to -1 --> IntegrityError (No New Order)
#         item.quantity = 1
#         item.unit_price = 10
#         item.save()

#     return render(request,'hello.html')

# # check the db:
# # select * from store_orderitem order by id desc;



# ---- Executing Raw SQL Queries ----


    # ----------objects.raw()

    # raw: Every manager has this raw method.
    # When you want to use raw SQL but still benefit from Django’s model layer.
    # Automatic mapping to Django model instances. 
    # Yani User.objects.raw("SELECT id, username FROM auth_user") yazarsan, 
    # dönen her satır bir User objesi gibi davranır (user.username, user.id diyebilirsin).


    # queryset = Product.objects.raw('select id,title from store_product')
    # return render(request, 'hello.html',{'products':queryset})

    # ----------connection.cursor()

    # When you need full control over SQL (e.g., complex joins, stored procedures, vendor-specific features).
    # When performance is critical and you want minimal ORM overhead.
    # When the query doesn’t map cleanly to a Django model.
    # from django.db import connection.

    # 1️⃣
    # cursor = connection.cursor()
    # cursor.execute('INSERT ...')
    # cursor.close()

    # 2️⃣ 
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, first_name FROM store_customer LIMIT 5")
        results = cursor.fetchall()

# results will look like:
# [(1, "Alice"), (2, "Bob"), (3, "Charlie"), ...]

    return render(request,'hello.html',{'products':results})
