# soru2:
# DESIRED OUTPUT
# ['D', 'NC', 'ZMP']

# ------a------

letters = []
with open("soru2.txt") as f:
    for line in f:
        row = ""
        for index in range(1, len(line), 4):
            row += line[index]
        letters.append(row.strip())

print(letters)

# ------b------
with open("soru2.txt") as f:
    letters = [line[1::4].strip() for line in f]

print(letters)
