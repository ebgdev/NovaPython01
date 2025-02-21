# desired_output: 
# name: Alice , age: 20
# name: Bob , age: 22
# name: Charlie , age: 19


# --------------------code-------------------

# with open("students.txt") as file:
#     for line in file:
#         name , age = line.strip().split(",")
#         print(f"name: {name} , age: {age}")


# --------------------code-------------------

# error : 3
# success: 3 
# warning: 2
# failed: 1

# from collections import Counter
# with open("log.txt") as f:
#     my_list = []
#     words = f.read().split()
#     count_words = Counter(words)
#     print(count_words.most_common(2))
#     for item,cntr in count_words.items():
#         print(f"{item}:{cntr}")



# --------------------code-------------------

# file = open("filename.txt", "mode")

# "r"	Read (default). File must exist.
# "w"	Write. Creates or overwrites a file.
# "a"	Append. Adds to the end of a file.
# "x"	Create. Creates a new file, fails if it exists.
# "b"	Binary mode (e.g., images, videos).
# "t"	Text mode (default).


# /Users/ma/Desktop/files in python/new_dir # absolute path
# if path starts with (./) means go from current folder/directory
# if path starts with (../) means go from previous folder/directory
# all these forward slashes should become backward slash for windows OS
# in order to get rid of all these changes we can use built-in hashlib tool
# https://docs.python.org/3/library/pathlib.html
# from pathlib import Path

# with open("new_dir/example.py") as f:  # relative path
#     for line in f:
#         print(line)


# --------------------code-------------------

import os  # isletim sistemi: Operation system
# # get working directory
# print("getcwd:", os.getcwd())
# print("get absolute path of log.py:", os.path.abspath("log.py"))
# print("dose zen.txt exists: ",os.path.exists("zen.txt"))
# print("dose info.txt exists: ",os.path.exists("info.txt"))
# working_path = os.getcwd()
# print("is it directory? ",os.path.isdir(working_path))
# print("is it file-1? ",os.path.isfile(working_path))
# print("is it file-2? ",os.path.isfile("log.py"))

# -------------------------------------

# def walk(dirname):
#     for name in os.listdir(dirname):
#         path = os.path.join(dirname, name)
#         if os.path.isfile(path):
#             print(path)
#         else:
#             walk(path)


# print(walk("/Users/ma/Desktop/"))


# # example_dir/
# # ├── file1.txt
# # ├── file2.txt
# # └── sub_dir/
# #     ├── file3.txt
# #     └── file4.txt

# # output:
# # example_dir/file1.txt
# # example_dir/file2.txt
# # example_dir/sub_dir/file3.txt
# # example_dir/sub_dir/file4.txt


# -----------------------------------------------
# import this # to see the zen of python
# ------------------------------------------------
# def fetch_lines(file_name):
#     with open(file_name) as f:
#         lines = []
#         for line in f:
#             lines.append(line)
#         return lines
    
# # print(fetch_lines("zen.txt"))


# def fetch_lines_yield(file_name):
#     with open(file_name) as f:
#         for line in f:
#             yield line

# zen = fetch_lines_yield("tl_usd_exchange_rate.csv")
# print(zen)

# for _ in range(1300000):
#     print(next(zen))


# # ----------------------------Buffering----------------------------
#### Buffering Nedir?
# Buffering, verilerin bir tamponda (hafızada) geçici olarak saklanması anlamına gelir.
# Bu tampon, dosyadan okuma veya dosyaya yazma işlemi sırasında kullanılır.
# Böylece disk erişimlerinin sayısı azalır ve performans artar.


# # ----------
# from time import time
# t1 = time()
# with open("novatext.txt") as f:
#     for line in f:
#         print(line)
# t2 = time()
# print(t2-t1)



# output = open("output.txt", "a")

# with open("tl_usd_exchange_rate.csv", buffering=1073741824) as f:
#     for line in f:
#         # print(line)
#         saveLine = line.replace("TL:USD ,", "")
#         output.write(saveLine)


# output.close()


# ------------------------------------------------
from icecream import ic
class Kedi:
    def __init__(self,name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


    def __str__(self):
        return f"{self.name} {self.age} yasinda"

    def __repr__(self):
        return f"name: {self.name} , age: {self.age} , breed = {self.breed}"
    
    def print_info(self):
        return self.name
    

leo = Kedi("leo",2,"domestic")
ic(leo)
ic(repr(leo))


age = input("enter your age: ")
ic(age)
ic(type(age))
ic(repr(age))
ic(leo.print_info())