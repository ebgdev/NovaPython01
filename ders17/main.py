from uzanti import Pet


class Cat(Pet):

    def __init__(self, owner, name, age, weight):
        super().__init__(name, age, weight)
        self.owner = owner

    def speak(self):
        return f"cat Created and make sound like bark mewo mewo"

    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}, Weight: {self.weight}, Owner: {self.owner}"
    

class Dog(Pet):

    def __init__(self, owner, name, age, weight):
        super().__init__(name, age, weight)
        self.owner = owner

    def speak(self):
        return f"dog Created and make sound like bark bark bark"

    


_1001 = Cat("erfan", "leo", 1, 6)
_1002 = Dog("enes", "pati", 2, 6)

print(_1001)
print(_1001.name)

print(str(_1001))
print(str(_1002))

print("###",_1001.speak())