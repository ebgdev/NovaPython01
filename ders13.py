# # # Ürünler ve fiyatları içeren sözlük
# # urunler = {
# #     'Laptop': 12000,
# #     'Telefon': 8000,
# #     'Tablet': 3500,
# #     'Akilli Saat': 2000,
# #     'Kulaklik': 750
# # }

# # def artan_sira(urunler):
# #     result = [list(urunler.items())[0]]  # Start with the first item in result list
# #     for coupe in list(urunler.items())[1:]:  # Iterate over the rest of the items
# #         coupe = list(coupe)
# #         inserted = False
# #         for i in range(len(result)):
# #             if coupe[1] < result[i][1]:
# #                 result.insert(i, coupe)  # Insert coupe in the correct position
# #                 inserted = True
# #                 break
# #         if not inserted:
# #             result.append(coupe)  # If not inserted, append at the end
# #     return dict(result)


# # def fiyat_sirala_azalan(urunler):
# #     sirali_urunler = dict(sorted(urunler.items(), key=lambda item: item[1],reverse=True))
# #     return sirali_urunler


# # print(artan_sira(urunler))
# # print(fiyat_sirala_azalan(urunler))

# # -------------------------------------------------------

# # countries = {
# #     'USA': {'Capital': 'Washington, D.C.', 'Population': 331000000, 'Language': 'English'},
# #     'France': {'Capital': 'Paris', 'Population': 67000000, 'Language': 'French'}
# # }

# # def manage_countries(action, country_name, info=None):
# #     if action == 'add':
# #         if country_name not in countries:
# #             countries[country_name] = info
# #             print(f"Added {country_name}.")
# #         else:
# #             print(f"{country_name} already exists.")
# #     elif action == 'update':
# #         if country_name in countries:
# #             countries[country_name].update(info)
# #             print(f"Updated information for {country_name}.")
# #         else:
# #             print(f"{country_name} not found.")
# #     elif action == 'get':
# #         if country_name in countries:
# #             print(f"Details for {country_name}: {countries[country_name]}")
# #         else:
# #             print(f"{country_name} not found.")
# #     else:
# #         print("Invalid action. Use 'add', 'update', or 'get'.")

# # # Example usage
# # manage_countries('add', 'Japan', {'Capital': 'Tokyo', 'Population': 126300000, 'Language': 'Japanese'})
# # manage_countries('update', 'France', {'Population': 68000000})  # Updates population of France
# # manage_countries('get', 'USA')  # Outputs details of USA

# # -----------------------------------------------------

# # Dictionary structure to store books in the library
# library = {
#     '1984': {'Author': 'George Orwell', 'Year': 1949, 'Available': True},
#     'To Kill a Mockingbird': {'Author': 'Harper Lee', 'Year': 1960, 'Available': True},
#     'The Great Gatsby': {'Author': 'F. Scott Fitzgerald', 'Year': 1925, 'Available': False},
# }

# # Function to add a new book
# def add_book(title, author, year):
#     if title not in library:
#         library[title] = {'Author': author, 'Year': year, 'Available': True}
#         print(f"Added '{title}' to the library.")
#     else:
#         print(f"The book '{title}' is already in the library.")

# # Function to update the availability of a book (borrow/return)
# def update_availability(title, status):
#     if title in library:
#         library[title]['Available'] = status
#         status_text = "available" if status else "borrowed"
#         print(f"Updated '{title}' status to {status_text}.")
#     else:
#         print(f"'{title}' not found in the library.")

# # Function to get information about a specific book
# def get_book_info(title):
#     if title in library:
#         print(f"Details of '{title}': {library[title]}")
#     else:
#         print(f"'{title}' not found in the library.")

# # Function to list all available books
# def list_available_books():
#     # Initialize an empty list to store available book titles
#     available_books = []
    
#     # Loop through each book in the library
#     for title, info in library.items():
#         # Check if the book is available
#         if info['Available']:
#             available_books.append(title)  # Add the title to the list of available books

#     # If there are available books, print them
#     if available_books:
#         print("Available books in the library:")
#         for book in available_books:
#             print(f"- {book}")
#     else:
#         print("No books are currently available.")


# # Example usage
# add_book('The Catcher in the Rye', 'J.D. Salinger', 1951)  # Adds a new book
# update_availability('1984', False)  # Marks '1984' as borrowed
# get_book_info('To Kill a Mockingbird')  # Retrieves details of a specific book
# list_available_books()  # Lists all available books


# ----------------------------------------------------------------
# pypi
# import pyjokes

# print(pyjokes.get_joke('en','neutral'))

# -----------------------------
# from collections import Counter,OrderedDict,defaultdict


# # ------------
# adict = {"enes":"electric eng","erfan":"bilgisayar eng"}
# bdict = {"erfan":"bilgisayar eng","enes":"electric eng"}


# d1 = OrderedDict()
# d2 = OrderedDict()

# d1["enes"] = "electric eng"
# d1["erfan"] = "bilgisayar eng"

# d2["erfan"] = "bilgisayar eng"
# d2["enes"] = "electric eng"


# print(adict == bdict)

# print(d1 == d2)

# # -----------------------------

# lst = ["banana","banana","apple","apple","apple","orange"]
# new_dict = Counter(lst)
# print(new_dict)

# # -----------------------------

# dictionary = defaultdict(lambda:"Dose Not Exist",{'a':1,'b':2})
# print(dictionary['c'])

# ----------------------------------------------------------------

# regular expressinos
# tum dillerde vardir
# validation like cheking somebody has entered the right email
# or password requirements
# or piece of string exist in piece of text

import re
# print(re)
# # -----------------------
# string = "search inside of this text please inside search"
# print("search" in string)
# # -----------------------
# string = "search inside of this text please inside search"

# print(re.search("search",string))
# a = re.search("pek",string)                     # olmadigi taktirde None degerini return yapar
# print("this is a:",a)                           # None

# b = re.search("inside of",string)
# print(b)                                        # var oldugu taktirde bir match.obj return yapar
# print(b.span())                                 # as tuple
# print(b.start())
# print(b.end())

# # the entire match
# print(b.group(0))                               # match.obj'ten eslenen stringi bulur ve return yapar
# --------------------------------------------

# pattern = re.compile("this")                    # This func compiles a regex pattern into a regex object
# print(pattern)                                  # bir kere compile edildikten sonra re-parse etmeksizin istedigimiz (daha verimli) zaman kullanabiliriz.

# string = "search this inside of this text please! and this"

# a = pattern.search(string)
# print(a)

# b = pattern.findall(string)
# print(b)

# c = pattern.fullmatch(string)
# print(c) # None

# pattern = re.compile(string)
# d = pattern.fullmatch(string)
# print(d) # returns match obj

# pattern = re.compile(string)
# d = pattern.fullmatch("search this inside of this text please! and this!")
# print(d) # None

# e = pattern.match("search this inside of this text please! and this and someimes this")
# print(e)

# --------------------------------------------

# peki suana kadar bir kac method ogrendik ama bunlar ne o kadar guclu nede o kadar onemli 
# soru -> peki neden her dil de bunlar var ?
# pattern gercekten neye yarar ona bir goz atalim.

# https://www.w3schools.com/python/python_regex.asp
# https://regex101.com/

# pattern = re.compile(r"([a-zA-Z]).([a])")
# string  = "search this inside of this text please! Erfan q@a"
# a = pattern.search(string)
# print(a.group(0)) 
# print(a.group(1))
# print(a.group(2))


# b = pattern.findall(string)
# print(b)
# for match in b:
#     print(match)

# d = pattern.finditer(string)
# for match in d:
#     print(match.group(0))  # Full match
#     print(match.group(1))  # First group
#     print(match.group(2))  # Second group


# --------------------------------------------
# # email validation
# # https://uibakery.io/regex-library/email-regex-python

# print(chr(97))
# print(chr(122))
# print(chr(65))
# print(chr(90))

# print(ord("a"))
# print(ord("z"))
# print(ord("A"))
# print(ord("Z"))

# pattern = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")

# string1 = "ebgdev@gmail.com"
# string2 = "herhangigmail.com"

# a = pattern.search(string1)
# if a:
#     print("Maches True")
# else:
#     print("Don't maches")

# ---------------------password-validation----------------------
# # At least 8 character 
# # Contain any sort letter , numbers or signs or symbols like %$#@
# # Has to end with a number

# pattern = re.compile(r"[A-Za-z0-9%$#@]{7,}\d$")

# var_str = "erfan123!6"
# print(len(var_str))
# a = pattern.match(var_str)
# print(a)


