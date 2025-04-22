from collections import deque
from icecream import ic 
# Create a deque
d = deque()
# Append to the right
d.append("emir")
d.append("adil")
d.append("fatih")
d.append("mess")

# Append to the left
d.appendleft("erfan")

ic(d)
# Pop from the right
d.pop()

# Pop from the left
d.popleft()
d.insert(1, "leo")
print(d)  # Output: deque([1, 2])
d.extend([4, 5])
d.extendleft([0, -1])
d.rotate(2)  # rotates 2 elements
ic("normal d:",d)
d.reverse()
ic("reversed d:",d)
print(len(d))

d_copy = d.copy()
d.index("leo")  # returns the element index
d.rotate() # rotate by one to the right side 
ic(d)

ic(len(d))


