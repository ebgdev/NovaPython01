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


# # ----------------------------9----------------------------
import os

# getcwd stands for get current working directory
print(os)
print("getcwd: ", os.getcwd())
file_txt_path = os.path.abspath("file.txt")
print("file.txt path: ", file_txt_path)
file_handler_py_path = os.path.abspath("file_handler.py")
print("file_handler.py path: ", file_handler_py_path)
print("existance: ", os.path.exists("file.txt"))
print("is direcory1: ", os.path.isdir(file_txt_path))
print("is file: ", os.path.isfile(file_txt_path))
print(
    "is direcory2: ",
    os.path.isdir("/Users/ma/Desktop/python addentionalls/files in python"),
)
print(
    "is direcory3: ",
    os.path.isdir("/Users/ma/Desktop/python addentionalls/files in python/file.txt"),
)
print("listing directories: ", os.listdir())

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

# # ----------------------------10----------------------------


# def fetch_lines(filename):
#     with open(filename, "r") as f:
#         lines = []
#         for line in f:
#             lines.append(line)
#         return lines


# zen = fetch_lines("zen.txt")
# print(zen)

# ---------------yield-keyword-----------------


# def fetch_lines(filename):
#     with open(filename, "r") as f:
#         for line in f:
#             yield line


# zen = fetch_lines("zen.txt")
# print(zen)  # generator object (yield)
# print(next(zen))
# print(next(zen)) # the previous line now erased


#####################################


# # ----------------------------Buffering----------------------------
#### Buffering Nedir?
# Buffering, verilerin bir tamponda (hafızada) geçici olarak saklanması anlamına gelir.
# Bu tampon, dosyadan okuma veya dosyaya yazma işlemi sırasında kullanılır.
# Böylece disk erişimlerinin sayısı azalır ve performans artar.


# # ----------


output = open("output.txt", "a")

with open("tl_usd_exchange_rate.csv", buffering=1073741824) as f:
    for line in f:
        # print(line)
        saveLine = line.replace("TL:USD ,", "")
        output.write(saveLine)


output.close()
