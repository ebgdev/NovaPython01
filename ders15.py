# -----------------cls-1----------------
# class Person:
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         # Alternative constructor
#         current_year = 2024
#         age = current_year - birth_year
#         return cls(name, age)

# person1 = Person("Alice", 30)
# person2 = Person.from_birth_year("Bob", 1990)

# print(person1.name, person1.age)  
# print(person2.name, person2.age)  


# -----------------cls-2----------------

# class Person():

#     def __init__(self,name,surname) -> None:
#         self.name = name
#         self.surname = surname

#     @classmethod
#     def init_with_str(cls,astr):
#         name, surname = astr.split(" ")
#         return cls(name,surname)
    
#     def p_info(self):
#         return f"name:{self.name} and surname: {self.surname}"




# erfan = Person.init_with_str("erfan bahcivan")
# print(erfan.p_info())

# ----------------------------------

# from datetime import date 


# class Car:
#     """aslinda burasi sadece bilgi vermeyi amaclayan bir alan"""
#     class_counter = 0
#     deneme = "deneme isimli bir string degisken"

#     def __init__(self, door, model, age):
#         self.door = door
#         self.model = model
#         self.age = age
#         self.class_counter += 1
#         Car.class_counter += 1

#     def p_info(self):
#         return(f'{self.model.capitalize()}({self.age}:age) --> {self.door} kapili')

#     @classmethod
#     def get_with_str(cls, str_):
#         door, model, age = str_.split("-")
#         return cls(int(door), model, int(age))

#     @classmethod
#     def get_with_year(cls, door, model, year):
#         return cls(door, model, date.today().year - year)

#     @classmethod
#     def cls_dende_erisiliyormus(cls):
#         return cls.deneme

#     def self_ilede_erisilebiliyormus(self):
#         return self.deneme


# masserati = Car(2, "quadroportre", 15)
# porsche = Car(4, "cayene", 12)
# bugatti = Car.get_with_str("2-divo-1")
# mclaren = Car.get_with_year(2, "F1", 1990)
# print(bugatti.age)
# print(bugatti.door)
# print(Car.class_counter)
# print(porsche.p_info())
# print(Car.p_info(masserati))
# print(bugatti.p_info())
# print(mclaren.p_info())
# print(Car.class_counter)
# # nesnenin global variable'ina erisimi var.
# print(masserati.deneme)
# print(bugatti.self_ilede_erisilebiliyormus())
# # @classmethod dan erisiliyor
# print(Car.cls_dende_erisiliyormus())
# # class'in kendisiden de erisiliyor
# print(Car.deneme)


######################################################

# OOP:
# Soyutlama (Abstraction)
# Kapsülleme (Encapsulation)
# Miras Alma (Inheritance)
# Çok Biçimlilik (Polymorphism)

# --------------------abstraction----------------------

# class PlayerCharacter():

#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age

#     def speek(self):
#         return f"my name is : {self.name} and im {self.age} year old."
        
# player1 = PlayerCharacter("Charlie",38)
# # player1.speek = "Hello"
# # print(player1.speek)
# print(player1.speek())


# --------------------encapsulation----------------------

#####################-information-#####################

# public    = variable (Fully accessible from anywhere)
# protected = _variable (Is for developers to know should only access inside class or subclass) still allows so not enfored.
# private   =  __variable (is to prevent from accidential access ) outside of class: only accessible with special method.

# ---------------------private--------------------

# class Person():
#     def __init__(self,name,age) -> None:
#         self.__name = name
#         self.__age = age

#     def name_getter(self):
#         return self.__name        
#     def age_getter(self):
#         return self.__age        
    
#     def name_setter(self,name):
#         self.__name = name

#     def age_setter(self,age):
#         self.__name = age

#     def display(self):
#         return f"name is : {self.__name} age is :{self.__age}"
    

# person = Person("Charlie", 40)

# # print(person.__name) # AttributeError
# # print(person._Person__name) # special way to access (modify,print) outside of class.
# print(person.name_getter())
# person.name_setter("erfan")
# print(person.display())


