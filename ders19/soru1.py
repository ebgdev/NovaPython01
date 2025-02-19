# soru1:
# DESIRED OUTPUT :
# [[10, 20, 30], [50, 60 70]]

# ------a------

numbers = []
with open("soru1.txt") as f:
    group = []
    for line in f:
        if line == "\n":
            numbers.append(group)
            group = []
        else:
            group.append(int(line.rstrip()))
    # append the last group because if line == "\n" will not be True for
    # the last group
    numbers.append(group)

print(numbers)

# ------b------

with open("soru1.txt") as f:
    # split input into groups based on empty lines
    groups = f.read().rstrip().split("\n\n")
    # convert all the values in the groups into integers
    nums = [list(map(int, (group.split()))) for group in groups]
print(nums)
