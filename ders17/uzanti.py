class Pet:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    # def __str__(self):
    #     return f"{self.name} can make sound"

    def speak(self):
        return f"Pet Created:{self.name} is {self.age} years old which is about {self.weight}"
    

if __name__ == "__main__":
    print(str(Pet))