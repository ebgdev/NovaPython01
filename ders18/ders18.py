class Employee():
    def __init__(self,name,id,age): # dunder veya magic methods
        self.name = name
        self.id = id
        self.age = age
        self.my_dict = {
            "field":"eng",
            "salary":"2600"
        }

    @classmethod
    def get_with_str(cls,astr):
        name, id ,age = astr.split("-")
        return cls(name,id,age)
    
    def print_info(self):
        return self.name
    
    def __str__(self):
        return f"{self.name}, {self.id} , {self.age}"
    
    def __repr__(self): # represent
        pass

    def __call__(self):
        return "employee is working..."

    # instance dunder method
    def __len__(self):
        return len(self.name)
    
    def __getitem__(self,item):
        return self.my_dict[item]
        

emp1 = Employee.get_with_str("erfan-1-27")
print(emp1.name)
print("emp1:",emp1)

print(len(emp1))

print(emp1())
print(emp1["salary"])

