# ## -------------------------------OOP---------------------------------

# # more info : https://en.wikipedia.org/wiki/History_of_programming_languages

# # everything in python is object
# print(type(None))
# print(type(True))
# print(type(5))
# print(type(3.3))
# print(type("hi"))
# print(type([]))
# print(type(()))
# print(type({}))

# # ve boylece biz nokta(.) kullanarak bir islem(action) uzerlerinde gerceklestirebiliriz.
# # objects have methods ands attributes that you can access with the dot method. ex: "hi".find()

# # CamelCase
# class BigObject: # class - sinif
#     pass


# obj1 = BigObject() # instanciate - ornekleme
# print(type(obj1))

## -------------------------------
# class PlayerCharacter():

#     membership = True    # static value so we dont want to change it later and it's accessible from instances and class itself.

#     def __init__(self,name,age) -> None:
#         # self here is a reference to the current instance of the class
#         # It allows us to access the attributes and methods of the object.
#         # For example, if we create an object like player1 = PlayerCharacter('John', 25),
#         # player1.name and player1.age will use 'self' to refer to the specific object's attributes.
#         print("class:",PlayerCharacter)
#         print("self:",self)
#         print(PlayerCharacter.membership)
#         print(self.membership)
#         self.name = name        # name attribute
#         self.age = age          # age attribute
        
#     def run(self):
#         # self allows us to refer to the object's methods and attributes inside the class.
#         # print(f'{name} run') # error cunku self ile name ozelligine erisebilirm
#         print(f'{self.name} run')
#         return "Done"


# player1 = PlayerCharacter("Michael",51)
# player2 = PlayerCharacter("Trevor",47)
# # print(PlayerCharacter.name)   # hata verir cunku instance object attributelar sadece objeler icindir
# print("membership on PlayerCharacter class: ",PlayerCharacter.membership)
# print("membership on player1: ",player1.membership)
# print("sinif:",PlayerCharacter)

# print(player1)        # object at a different address
# print(player2)        # object at a difference address

# # help(PlayerCharacter) 


## -------------------------------
# from datetime import datetime           
# from re import compile, search, match
# import random
# import string

# class Toyota:

#     # class object attribute 
#     guarantee = True
#     class_counter = 0 

#     # A constructor is a special method that is used to initialize objects.
#     def __init__(self, name="anonymous", door=4) -> None:
#         print("here is self: ", self)
#         self.name = name
#         self.door = door
#         self.creation_time = datetime.now()
#         self.chassis_number = self.generate_chassis_no()
#         Toyota.class_counter +=1

#     # instance method
#     def generate_chassis_no(self):
        
#         letters_part1 = ''.join(random.choices(string.ascii_uppercase, k=3))
#         digits_part2 = ''.join(random.choices(string.digits, k=6))
#         chassis_no = f"{letters_part1}{digits_part2}"
#         pattern = compile(r'^[A-Z]{3}\d{6}$')
        
#         if pattern.match(chassis_no):
#             return chassis_no
#         else:
#             return "Invalid chassis number"

#     # instance method
#     def p_information(self):
#         return f'Car Name: {self.name} ,Door Count: {self.door} ,Product Date: {self.creation_time}, Chassis Number: {self.chassis_number} '

#     # static method
#     def slogan():
#         return("Let's Go Places") 

# car1 = Toyota("Corolla")
# car2 = Toyota("Land Cruiser", 5)
# print("car1: ", car1)
# print("car2: ", car2)
# print("car1 name: ", car1.name)
# print("car1 door: ", car1.door)
# print("car2 name: ", car2.name)
# print("car2 door: ", car2.door)
# print("car1 creation time: ", car1.creation_time)
# print("car1 chassis number: ", car1.chassis_number)
# print("car2 chassis number: ", car2.chassis_number)
# print("car2 information: ", car2.p_information())
# print("car2 slogan:",Toyota.slogan())
# print("this is class counter",Toyota.class_counter)


# car2.fwd = True
# print("car2 fwd: ", car2.fwd)

## --------------with-static----------------

# class Apple:
#     def __init__(self, model):
#         self.model = model

#     @staticmethod
#     def about_apple():
#         print("Apple Inc. is a tech company.")

# # You can call it directly from the class
# Apple.about_apple()

# iphone = Apple("iPhone")
# iphone.about_apple()



## --------------without-static----------------

# class Apple:
#     def __init__(self, model):
#         self.model = model

#     # This is treated as a regular instance method
#     def about_apple(self):
#         print("Apple Inc. is a tech company.")

# # You must instantiate the class to call the method
# iphone = Apple("iPhone")
# iphone.about_apple()



# ----------------------------------
# from datetime import datetime

# class Apple():
    
#     def __init__(self,model) -> None:
#         self.model = model
#         self.release_year = datetime.now().year
#         self.update_support_date = datetime.now().year + 5

#     @classmethod
#     def adding_things(cls,num1,num2):
#         return cls(num1+num2)

# iphone5 = Apple("iphone5")

# print(iphone5.release_year)
# print(iphone5.update_support_date)
# print(Apple.adding_things("iphone","6").model)
# print(Apple.adding_things("iphone","6").release_year)


# ----------------------------------
# from datetime import datetime

# class Apple():
    
#     def __init__(self,model,ornek) -> None:
#         self.model = model
#         self.ornek = ornek

#     @classmethod
#     def adding_things(cls,model,num1,num2):
#         return cls(model,num1+num2)

# iphone5 = Apple("iphone5","ornek1")

# print(Apple.adding_things("iphone6","ornek","2").ornek)


# ----------------------------------

from datetime import date


class Car:
    """aslinda burasi sadece bilgi vermeyi amaclayan bir alan"""
    class_counter = 0
    deneme = "deneme isimli bir string degisken"

    def __init__(self, door, model, age):
        self.door = door
        self.model = model
        self.age = age
        self.class_counter += 1
        Car.class_counter += 1

    def p_info(self):
        return(f'{self.model.capitalize()}({self.age}:age) --> {self.door} kapili')

    @classmethod
    def get_with_str(cls, str_):
        door, model, age = str_.split("-")
        return cls(int(door), model, int(age))

    @classmethod
    def get_with_year(cls, door, model, year):
        return cls(door, model, date.today().year - year)

    @classmethod
    def cls_dende_erisiliyormus(cls):
        return cls.deneme

    def self_ilede_erisilebiliyormus(self):
        return self.deneme


masserati = Car(2, "quadroportre", 15)
porsche = Car(4, "cayene", 12)
bugatti = Car.get_with_str("2-divo-1")
mclaren = Car.get_with_year(2, "F1", 1990)
print(bugatti.age)
print(bugatti.door)
print(Car.class_counter)
print(porsche.p_info())
print(Car.p_info(masserati))
print(bugatti.p_info())
print(mclaren.p_info())
print(Car.class_counter)
# nesnenin global variable'ina erisimi var.
print(masserati.deneme)
print(bugatti.self_ilede_erisilebiliyormus())
# @classmethod dan erisiliyor
print(Car.cls_dende_erisiliyormus())
# class'in kendisiden de erisiliyor
print(Car.deneme)
