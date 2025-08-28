from itertools import permutations


def generate_permutations(arr):
    counter = 0
    perm_list = list(permutations(arr))  # Generate all possible permutations
    print(perm_list)

    for perm in perm_list:
        counter += 1
        print(perm)
    return f"islem sayisi: {counter}"


# Example usage:
arr = [1, 2, 3, 4, 5]
#      5* 4* 3* 2* 1 = 5! = 120

print(generate_permutations(arr))
