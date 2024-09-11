# numbers = [3, 5, 7, 10, 15, 20, 25]

# kareli_sayilar = list(map(lambda x: x ** 2, numbers))
# print("Kareli sayilar:", kareli_sayilar)

# ters_liste = []
# i = len(kareli_sayilar) - 1
# while i >= 0:
#     ters_liste.append(kareli_sayilar[i])
#     i -= 1
# print("Ters çevrilmiş liste:", ters_liste)

# filtrelenmis_liste = list(filter(lambda x: x >= 50, ters_liste))
# print("Filtrelenmiş liste (50 >= sayilar):", filtrelenmis_liste)


# --------------------------------------------

# mixed_data = [12, 'hello', 3.5, 42, 'world', 99, 0.1, 'Python', 23]


# filterlenmis_veri = filter(lambda x: type(x) == int, mixed_data)
# tamsayilar_10_ile_carp = list(map(lambda x: x * 10, filterlenmis_veri))
# print("10 ile carpilmis tamsayilar:", tamsayilar_10_ile_carp)

# for index, value in enumerate(mixed_data):
#     if type(value) == int and value % 2 == 0:
#         continue
#     print(f"İndeks: {index}, Değer: {value}")


# ters_liste = []
# for item in mixed_data:
#     ters_liste.insert(0, str(item))
# print("Ters çevrilmiş liste, öğeler string olarak:", ters_liste)
# -------------------Tuple-0------------------

# ordered and immutable 
# yani sirasina gore elemanlara erisebiliriz 
# ve elemanlar degistirilemez
# degistirmeye ihtiyacimiz olmayan bir yerde kullanabiliriz
# daha hizlidirlar ve daha az yer kapsarlar

# my_list = ["bir","iki","uc","dort"]
# print(my_list[0])
#------------
# first_tuple = ("bir",)
# second_tuple = ("iki","uc","dort")
# print(first_tuple[0])
# print(type(first_tuple))
#------------
# my_list[0] = 1
# print(my_list)

## first_tuple[0] = 1 # hata uretir cunku degistirilemez

# yeni_tuple = ("erfan","arslan","hamit",["ahmet","mehmet"])

# yeni_tuple[3][1] = "dogan"

# print(yeni_tuple)

# -------------------Tuple-1------------------

# my_list = [1,2,3,4]
# my_list.append(5)
# print(my_list)

# my_tuple = (1,2,3,4)
# my_tuple.append(5)    # hata ailriz cunku tuple objelerin append ozellikleri yok

# -------------------Tuple-space------------------
# import sys

# my_list = [i for i in range(0,1000000)]
# my_tuple = tuple(i for i in range(0,1000000))


# print(my_list)
# print(my_tuple)


# print(sys.getsizeof(my_list))
# print(sys.getsizeof(my_tuple))


# -------------------Tuple-speed------------------

# import timeit

# print(timeit.timeit(stmt='("red","blue","green","erfan",1,2,3,4,5)',number = 100000000))
# print(timeit.timeit(stmt='["red","blue","green","erfan",1,2,3,4,5]',number = 100000000))

# --------------------emergency-add-1-----------------------

# my_tuple = ("new_iphone","new_ipad","new_mac","new_watch","new_airpod","new_apple_tv")

# convert_to_tuple = list(my_tuple)
# print(convert_to_tuple)
# convert_to_tuple.append("new_apple_vision")
# my_tuple = tuple(convert_to_tuple)
# print(my_tuple)

# --------------------emergency-add-2-----------------------

# my_tuple = ("new_iphone","new_ipad","new_mac","new_watch","new_airpod","new_apple_tv")
# my_tuple += ("new_iphone","new_ipad","new_mac","new_watch","new_airpod","new_apple_tv","new_apple_vision")

# print(my_tuple)

# ---------------------avalible-methods-----------------------

# assumed_tuple = (1,)
# assumed_list = [1]


# print(len(dir(assumed_tuple)))
# print(len(dir(assumed_list)))

# --------------------------------------------
# sets are distinct and unordered

# my_set = {1,1,1,2,2,2,3,41,5,6,7,2,12,23,543,6423}
# print(my_set)

# for i in range(len(my_set)):
# 	print(my_set[i])   # unorderd oldugundan dolayi hata aliriz
# 	print()


# for i in my_set:
# 	print(i)

# cikti sirasina hic bir zaman guvenemeyiz surekli degisebilir
# myset = {"Geeks", "for", 10, 52.7, True}
# print(myset)


# --------------------set-----------------------


# aset = {"erfan", "alperen", "mess","taha"}
# print(aset)

# aset.add("anil")          	# eleman ekler
# aset.remove("yasemin")   		# eleman varsa siler ama olmayan eleman icin remove hata uretir
# aset.discard("yasemin")   	# eleman varsa siler ama olmayan eleman icin remove hata uretmez
# random_deger = aset.pop()     # pop farazi bir elemani siler ve onu donderir her sefeerinde bu degisebilir
# print(random_deger) 
# print(aset)
# bset = {"erfan","alperen","arda"}
# print(aset|bset)   						# union (matematiksel gosterim) 
# print(aset.union(bset))                 # union
# print(aset.intersection(bset))        	# ortaklari verir
# print(aset & bset)                      # ortaklari verir (matematiksel gosterim)
# print(aset.difference(bset))            # a seti uzerindeki olan ve b setinde olmayan eleman yani farklarini  
# print(aset - bset)                      # a seti uzerindeki olan ve b setinde olmayan eleman yani farklarini  (matematiksel gosterim)
# print(aset.issubset(bset))              # alt kumesi mi
# print(aset.issuperset(bset))			  # ust kumesi mi
# fs = frozenset([1,2,3,4,4,5,1,2])
# fs.add(10)
# --------------------dict-veya-hash---------------------

# dictionary --> orderd and mutable (changeble)

# my_dict = {"turkey":99,"usa":1,"canada":1,"germany":45}

# print(my_dict.get("turkey"))
# print(my_dict["turkey"])


# print(my_dict.get("eygpt"))                           # olmayan eleman icin None degerini dondurur
# print(my_dict.get("eygpt", "eleman bulunamadi"))      # olmayan eleman icin None degerini dondurur
# print(my_dict["eygpt"])                               # olmayan eleman icin hata uretir

# print(my_dict.items())
# print(list(my_dict.items())[0])


# print(my_dict.keys())
# print(my_dict.values())

# print(my_dict.pop("efefe","ljefe"))
# print(my_dict)

# print(my_dict.pop("germany"))
# print(my_dict)


# print(my_dict.popitem())                             # sadece son elemani siler
# print(my_dict)

# my_dict.update({"india": 91})
# print(my_dict)

# my_dict.update({"usa": 2})
# print(my_dict)



# -----------------------------merge-dictionaries-------------------------------

# def merge_dicts(d1, d2):
#     d1.update(d2)
#     merged = d1
    
#     return merged

# # Example
# d1 = {'a': 1, 'b': 2}
# d2 = {'b': 3, 'c': 4}
# print(merge_dicts(d1, d2))  # Output: {'a': 1, 'b': 3, 'c': 4}

# -----------------------------common-elements-------------------------------

# def common_elements(lst1, lst2):
#     return list(set(lst1).intersection(set(lst2)))

# # Example
# lst1 = [1, 2, 3, 4]
# lst2 = [3, 4, 5, 6]
# print(common_elements(lst1, lst2))  # Output: [3, 4]


# -----------------------------remove-duplicates-------------------------------

# def remove_duplicates(tpl):
#     return tuple(set(tpl))


# tpl = (1, 2, 2, 3, 4, 4)
# print(remove_duplicates(tpl))  # Output: (1, 2, 3, 4)