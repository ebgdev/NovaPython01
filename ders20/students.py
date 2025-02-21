with open("students.txt", "r") as file:
    for line in file:
        name, age = line.strip().split(", ")
        print(f"Name: {name}, Age: {age}")
