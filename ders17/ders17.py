# --------------------------------dunder method---------------------------------

# print(dir(int))
# print(id(str(32.1)))
# print(id(32.1.__str__()))


# ---------------

# class Toy():
#     def __init__(self,color,age) -> None:
#         self.color = color
#         self.age = age


# action_figure = Toy('red',0)
# print(action_figure.__str__)   # method-wrapper
# print(action_figure.__str__())
# print(str(action_figure))

# ---------------

# class Toy:
#     def __init__(self,color,age,name):
#         self.color = color
#         self.age = age
#         self.name = name
#         self.my_dict = {
#             'name':'barby',
#             'yan_urunler':True
#         }

#     def __str__(self):
#         return self.color
    

#     def __len__(self):
#         return len(self.name)
    
#     def __call__(self):
#         return "cagrildim"
    
#     def __getitem__(self,i):
#         return self.my_dict[i]

# action_figure = Toy('red',0,"python ogreniyoruz")
# print(action_figure.__str__())
# print(str(action_figure))
# print(len(action_figure))
# print(len("helloworld!!!!"))
# print(action_figure())
# print(action_figure['name'])

# ----------------------dunder----------------------

# class MyClass:
#     @classmethod
#     def from_name(cls, name):
#         obj = cls.__new__(cls)  # Bypass __init__
#         obj.name = name  # Set attributes directly
#         return obj

#     @classmethod
#     def from_age(cls, age):
#         obj = cls.__new__(cls)
#         obj.age = age
#         return obj

# # Creating objects using class methods
# obj1 = MyClass.from_name("Alice")
# obj2 = MyClass.from_age(30)

# print(obj1.name)  # Output: Alice
# print(obj2.age)   # Output: 30
