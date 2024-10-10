
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner          
#         self.__balance = balance    

#     # public instance method
#     def deposit(self, amount):  
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}. New balance is {self.__balance}")
#         else:
#             print("Deposit amount must be positive!")

#     # private instance method
#     def __apply_interest(self):  
#         self.__balance *= 1.02
#         return self.__balance

#     # public instance method
#     def get_balance(self):  # Public method that uses private method
#         self.__apply_interest()  # Private method called inside public method
#         return self.__balance
    

# account = BankAccount("erfan",100000)
# account.deposit(200)
# print(account._BankAccount__apply_interest())
# print(account.get_balance())

# ---------------------------------------------------


# class Person:
#     def __init__(self,name,lastname) -> None:
#         self.name = name
#         self.lastname = lastname
    
#     @classmethod
#     def instructor(cls,astr):
#         astr = cls.name , cls.lastname
    

#     def addidas():
#         return "this is addidas"
#     @staticmethod
#     def nike():
#         return "this is nike"
    
#     def yazdir(self):
#         return (f"name: {self.name}, soyad: {self.lastname}")


# kisi = Person("erfan","bahcivan")
# print(kisi.name)
# kisi.name = "nova"
# kisi.yazdir = "selam"
# print(kisi.yazdir())
# kisi.yazdir = "selam"


# ---------------------------inheritance---------------------------

# class User():
#     def sign_in(self):
#         return "logged in"
    

# class Ogretmen(User):
#     def __init__(self,name,gereksinim):
#         self.name = name
#         self.gereksinim = gereksinim
#     # instanciate method
#     def konus(self):
#         return f"bir ogretmenin gereksinimi: \nlisans seviyesi\nen az {self.gereksinim *2} saat calismasi"
    

# class Ogrenci(User):
#     def __init__(self,name,gereksinim):
#         self.name = name
#         self.gereksinim = gereksinim
#     # instanciate method
#     def konus(self):
#         return f"bir ogrenci gereksinimi: \nlise seviyesi\nen az {self.gereksinim} saat calismasi"
    

# ogretmen = Ogretmen("erfan",5)
# ogrenci = Ogrenci("anil",5)

# print("ogrenci",ogrenci.sign_in())
# print("ogretmen",ogretmen.sign_in())

# print("ogrenci konus:",ogrenci.konus())
# print("ogretmen konus:",ogretmen.konus())

# print(isinstance(ogrenci,User))
# print(isinstance(ogrenci,Ogrenci))

# print(issubclass(Ogrenci,User))
# print(issubclass(Ogrenci,Ogretmen))


# -------------------------------------
# class Parent:
#     pass

# class Child(Parent):
#     pass

# new_kid = Child()
# print(new_kid)


# print(isinstance(new_kid,Child))
# print(issubclass(Child,Parent))

# ------------------------------------------------------
# class Deneme():
#     pass


# deneme = Deneme()

# print(isinstance(deneme,Deneme))
# print(isinstance(deneme,object))

# ----------------------------polymorphism-----------------------------

# class User:

#     def sign_in(self):
#         return('logged in')
    
#     # def konus(self):
#     #     print(f"User sinifindan uretilen obje konusur")

# class Ogrenci(User):
#     def __init__(self,name,gereksinim) -> None:
#         self.name = name
#         self.gereksinim = gereksinim

#     def konus(self):
#         # User.konus(self)
#         return f"bir ogrencinin gereksinimi: \n-lise seviyesi\n-en az {self.gereksinim*1} saat calismasi."

# class Ogretmen(User):
#     def __init__(self,name,gereksinim) -> None:
#         self.name = name
#         self.gereksinim = gereksinim

#     def konus(self):
#         return f"bir ogrencinin gereksinimi: \n-lisans seviyesi\n-en az {self.gereksinim*2} saat calismasi."


# ogrenci1 = Ogrenci("fatih",5)
# ogretmen1 = Ogretmen("erfan",5)


# def user_speak(user):
#     return user.konus()


# print(user_speak(ogretmen1))
# print(user_speak(ogrenci1))

# ----------------------super-----------------------

# class User:

#     def __init__(self,email) -> None:
#         self.email = email

#     def sign_in(self):
#         return('logged in')
    
#     # def konus(self):
#     #     print(f"User sinifindan uretilen obje konusur")

# class Ogrenci(User):
#     def __init__(self,name,gereksinim,email) -> None:
#         User.__init__(self,email)
#         self.name = name
#         self.gereksinim = gereksinim

#     def konus(self):
#         # User.konus(self)
#         return f"bir ogrencinin gereksinimi: \n-lise seviyesi\n-en az {self.gereksinim*1} saat calismasi."

# class Ogretmen(User):
#     def __init__(self,name,gereksinim,email) -> None:
#         super().__init__(email)
#         self.name = name
#         self.gereksinim = gereksinim

#     def konus(self):
#         return f"bir ogrencinin gereksinimi: \n-lisans seviyesi\n-en az {self.gereksinim*2} saat calismasi."


# ogrenci1 = Ogrenci("fatih",5,"fatih.stu.nova@gmail.com")
# ogretmen1 = Ogretmen("erfan",5,"erfan.nova@gmail.com")


# print(ogrenci1.email)
# print(ogretmen1.email)
