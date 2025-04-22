from llist import sllist, dllist

# ---------------------------
# Singly Linked List Example
# ---------------------------
print("=== Singly Linked List (sllist) ===")
slist = sllist([1, 2, 3])
print("Original list:")
for node in slist:
    print(node)

# Append to end
slist.append(4)

# Append to front
slist.appendleft(0)

print("\nAfter append and appendleft:")
for node in slist:
    print(node)

# Access first and last elements
print("\nFirst element:", slist.first.value)
print("Last element:", slist.last.value)

# Remove second element (value 1)
slist.remove(slist.first.next)

print("\nAfter removing second element (value 1):")
for node in slist:
    print(node)

# ---------------------------
# Doubly Linked List Example
# ---------------------------
print("\n=== Doubly Linked List (dllist) ===")
dlist = dllist([10, 20, 30])
print("Original list:")
for node in dlist:
    print(node)

# Append to end
dlist.append(40)

# Append to front
dlist.appendleft(5)

print("\nAfter append and appendleft:")
for node in dlist:
    print(node)

# Access first and last elements
print("\nFirst element:", dlist.first.value)
print("Last element:", dlist.last.value)

# Remove second element (value 10)
dlist.remove(dlist.first.next)

print("\nAfter removing second element (value 10):")
for node in dlist:
    print(node)
