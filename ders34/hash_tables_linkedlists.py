class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, head in enumerate(self.data_map):
            values = []
            current = head
            while current:
                values.append([current.key, current.value])
                current = current.next
            print(i, ":", values)

    def set_item(self, key, value):
        index = self.__hash(key)
        new_node = Node(key, value)
        if self.data_map[index] is None:
            self.data_map[index] = new_node
        else:
            current = self.data_map[index]
            while current:
                if current.key == key:
                    current.value = value  # update existing key
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def get_item(self, key):
        index = self.__hash(key)
        current = self.data_map[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def keys(self):
        all_keys = []
        for index in self.data_map:
            current = index
            while current:
                all_keys.append(current.key)
                current = current.next
        return all_keys

    def values(self):
        all_values = []
        for index in self.data_map:
            current = index
            while current:
                all_values.append(current.value)
                current = current.next
        return all_values

    def items(self):
        all_items = []
        for index in self.data_map:
            current = index
            while current:
                all_items.append((current.key, current.value))
                current = current.next
        return all_items


# Example usage
my_hash_table = HashTable()

my_hash_table.set_item("books", 1000)
my_hash_table.set_item("markers", 100)
my_hash_table.set_item("notebooks", 300)
my_hash_table.set_item("pens", 200)
my_hash_table.set_item("pencils", 300)

my_hash_table.print_table()

# print(my_hash_table.get_item("books"))
# print(my_hash_table.get_item("markers"))
# print(my_hash_table.get_item("pencils"))
# print(my_hash_table.get_item("notebooks"))

print(my_hash_table.keys())
# print(my_hash_table.values())
# print(list(my_hash_table.items()))
