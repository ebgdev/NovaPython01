import random
import string
class Pet:
    def __init__(self,breed,name,age):
        self.breed = breed
        self.name = name
        self.age = age
        self.__chip_id = self.generate_random_id()

    def __str__(self):
        return self.name
    
    def chip_id_getter(self):
        return self.__chip_id

    @staticmethod
    def generate_random_id(length = 8):
        characters = string.ascii_letters + string.digits
        return "".join(random.choice(characters) for i in range(length))

if __name__ == "__main__":
    
    dog1 = Pet("chow chow","milo",8)
    print(dog1.chip_id_getter())