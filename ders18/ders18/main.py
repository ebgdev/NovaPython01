from file import Pet

class Dog(Pet):
    def __init__(self, breed, name, age,sound):
        super().__init__(breed, name, age)
        self.sound = sound

    def __str__(self):
        return self.sound


class Snake(Pet):
    def __init__(self, breed, name, age):
        super().__init__(breed, name, age)

dog1 = Dog("chow chow","milo",8,"hav hav")
snake1 = Snake("python","zerdecal",3)
print(dog1.chip_id_getter())
print(snake1.chip_id_getter())