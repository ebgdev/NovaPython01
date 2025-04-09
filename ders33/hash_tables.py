class HashTable:
    def __init__(self,size=7):
        self.data_map = [None] * size

    def __hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i,":",val)

    def set_item(self,key,value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self,key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                # so if the key matches
                if self.data_map[index][i][0] == key:
                    # we will return the value for that key
                    return self.data_map[index][i][1]
        return None
    
    # return list of all keys 
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    

    def values(self):
        all_values = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_values.append(self.data_map[i][j][1])
        return all_values
    
    def items(self):
        all_items = []
        for bucket in self.data_map:
            if bucket is not None:
                for pair in bucket:
                    all_items.append((pair[0], pair[1]))
        return all_items

        



my_hash_table = HashTable()

my_hash_table.set_item("books",1000)
my_hash_table.set_item("markers",100)
my_hash_table.set_item("notebooks",300)
my_hash_table.set_item("pens",200)
my_hash_table.set_item("pencils",300)

my_hash_table.print_table()

print(my_hash_table.get_item("books"))
print(my_hash_table.get_item("markers"))
print(my_hash_table.get_item("pencils"))
print(my_hash_table.get_item("notebooks"))

print(my_hash_table.keys())
print(my_hash_table.values())
print(list(my_hash_table.items()))