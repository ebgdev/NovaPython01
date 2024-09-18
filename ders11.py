# # ----------------------------

# def count_frequency(lst):
#     my_dict = {}
#     for item in lst:
#         if my_dict.get(item) != None:  
#             my_dict[item] += 1  
#         else:
#             my_dict[item] = 1  
#     return my_dict


# # lst = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
# # print(count_frequency(lst))  # Output: {'apple': 2, 'banana': 3, 'orange': 1}


# # -----------------------------group-by-frequency-------------------------------

# def group_by_frequency(frequency):
#     grouped = {}
#     for item, freq in frequency.items():
#         if freq not in grouped:
#             grouped[freq] = []
#         grouped[freq].append(item)
#     return grouped

# # Example
# lst = ['a', 'b', 'b', 'c', 'c', 'c']
# print(count_frequency(lst))
# print(group_by_frequency(count_frequency(lst)))  # Output: {1: ['a'], 2: ['b'], 3: ['c']}


# ----------------------------

musteriler = {
    1000000001: {
        'name': 'John',
        'sur_name': 'Doe',
        'age': 17,
        'married': False
    },
    1000000002: {
        'name': 'Jane',
        'sur_name': 'Smith',
        'age': 16,
        'married': True
    },
    1000000003: {
        'name': 'Alice',
        'sur_name': 'Brown',
        'age': 22,
        'married': False
    },
    1000000004: {
        'name': 'Bob',
        'sur_name': 'Johnson',
        'age': 45,
        'married': True
    },
    1000000005: {
        'name': 'Charlie',
        'sur_name': 'Williams',
        'age': 30,
        'married': True
    },
    1000000006: {
        'name': 'Eve',
        'sur_name': 'Davis',
        'age': 27,
        'married': False
    },
    1000000007: {
        'name': 'Mike',
        'sur_name': 'Miller',
        'age': 40,
        'married': True
    },
    1000000008: {
        'name': 'Nancy',
        'sur_name': 'Wilson',
        'age': 15,
        'married': True
    },
    1000000009: {
        'name': 'James',
        'sur_name': 'Taylor',
        'age': 21,
        'married': False
    },
    1000000010: {
        'name': 'Olivia',
        'sur_name': 'Anderson',
        'age': 38,
        'married': True
    }
}

# ------------------------print-names-------------------------

# for i in musteriler:
#     print(musteriler[i]["name"])


# # list(map(lambda person: print(person["name"]), musteriler.values()))
# print(list(map(lambda person: person["name"], musteriler.values())))

# -----------------------yas-ortalama-------------------------

# import statistics

# ages = list(map(lambda x: x["age"], musteriler.values()))

# print(round(statistics.mean(ages)))


# def yas_ortalama(musteriler):
#     length = len(musteriler)
#     yas_ortalama = 0
#     for i in musteriler.values():
#         yas_ortalama+=i["age"]

#     return yas_ortalama//length

# print(yas_ortalama(musteriler))


# -----------------------kac-evli-------------------------

# def evli_sayisi(musteriler):
#     sayac = 0
#     for musteri in musteriler.values():
#         if musteri["married"]:
#             sayac+=1
#     return sayac

# print(evli_sayisi(musteriler))

# print(len(list(filter(lambda x: x["married"] == True, musteriler.values()))))


# -----------------------yas-18-ustu------------------------

# def up_18(musteriler):
#     granted_persons = []
#     musteri_bilgileri = list(musteriler.values())
#     for i in range(len(musteri_bilgileri)):
#         if musteri_bilgileri[i]["age"] >= 18:
#             print(f'{musteri_bilgileri[i]["name"]} {musteri_bilgileri[i]["sur_name"]} izin verildi.')
#             granted_persons.append(list(musteriler.keys())[i])
#         else:
#             print(f'{musteri_bilgileri[i]["name"]} {musteri_bilgileri[i]["sur_name"]} izin verilmedi.')
#     return granted_persons


# print(up_18(musteriler))

# -----------------------group_by_first_letter(words)------------------------

def group(musteriler):
    yeni_group = {}
    for details in musteriler.values():  
        first_letter = details['name'][0]  
        if first_letter not in yeni_group:
            yeni_group[first_letter] = []
        yeni_group[first_letter].append(details['name'])
    return yeni_group

print(group(musteriler))

# -----------------------group_by_first_letter(words)------------------------

# words = ['apple', 'banana', 'grape', 'apricot', 'berry', 'cherry']
# # output: {'a': ['apple', 'apricot'], 'b': ['banana', 'berry'], 'g': ['grape'], 'c': ['cherry']}

# def group_by_first_letter(words):
#     my_dict = {}
#     for word in words:
#         if word[0] in my_dict:
#             my_dict[word[0]].append(word)  # Append the word to the existing list
#         else:
#             my_dict[word[0]] = [word]  # Initialize a new list with the word
#     return my_dict

# print(group_by_first_letter(words))

# ----------------------------------------------------

# def example_function(**kwargs):
#     print(kwargs)

# example_function(name="yasemin", age=30, city="samsun")


# ----------------------------------------------------

# def greet(**kwargs):
#     if "name" in kwargs:
#         print(f"Hello, {kwargs['name']}!")
#     if "age" in kwargs:
#         print(f"You are {kwargs['age']} years old.")

# greet(name="ali", age=25)
# greet(name="adem")

# ----------------------------------------------------

# def person_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# person_info(name="Ali", age=30, city="samsun")


# ----------------------------------------------------

# def mixed_function(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# mixed_function(1, 2, 3, name="Ali", age=30)

# ----------------------------------------------------

# from hashlib import sha256

# input_ = input('Enter something: ')
# print(sha256(input_.encode('utf-8')).hexdigest())