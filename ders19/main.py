# # ------------------------------1----------------------------
# f = open("file.txt")
# # -----------
# # print(f.read()) # read(num) , num -> kac tane karakter okumasi gerekli.
# # print(f.read()) # bir kez onceden okudugu icin artik end of file'a geldi ve burasi bos bir cikti verir
# # -----------

# file = open("file.txt")
# print("1.", file.read()) # the cursor starts from 0 position and gets to the end of file
# file.seek(0)  # puts the cursor to the 0 position.
# print("2.", file.read()) # now the cursor is at the start which is 0.index and it's ready to read

# # -----------
# # print(f.readline())
# # print(f.readline())
# # -----------

# f.close()  # acilan her dosyayi islem bittikten sonra kapatarak yanlisliklarin onune geceriz.


# ----------------------next-keyword---------------------

# file = open("file.txt")
# print(next(file))
# file.close()

# -------------------

# file = open("file.txt")
# for i in range(5):
#     print(next(file))
# file.close()


# ----------------------close-automatically---------------------

# -----------------

# with open(
#     "file.txt"
# ) as f:  # by using the with/as format to open files, we get rid of the need to call f.close() manually.
#     line1 = next(f)
#     print(line1)

#     line2 = next(f)
#     print(line2)

# -----------------

# with open(
#     "file.txt"
# ) as f:  # by using the with/as format to open files, we get rid of the need to call f.close() manually.
#     for line in f.readlines():
#         print(line)

# -----------------class-method--------------------


# class Car:
#     def __init__(self, factory, model, engine, seat, door, Vtype):
#         self.factory = factory
#         self.model = model
#         self.engine = engine
#         self.seat = seat
#         self.door = door
#         self.Vtype = Vtype

#     @classmethod
#     def get_with_str(cls, astr):
#         factory, model, engine, seat, door, Vtype = astr.split(",")
#         return cls(factory, model, engine, seat, door, Vtype)


# with open("information.txt", "r") as file:
#     lines = file.readlines()

# objects = {}
# for i in range(len(lines)):
#     line = lines[i]
#     objects[f"car{i}"] = Car.get_with_str(line)


# print(objects["car1"].factory)
# print(objects["car1"].model)

# -----------------------------------------------
