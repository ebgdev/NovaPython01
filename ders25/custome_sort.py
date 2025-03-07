array = [56,98,-100,985,285]
names = ["fatih","adil","emir","taha","mess"]


def minimum(lst):
    min_value = lst[0]
    for item in lst:
        if item < min_value:
            min_value = item
    return min_value


def custome_sort(lst):
    a = []
    for _ in range(len(lst)):
        min_value = minimum(lst)
        a.append(min_value)
        lst.remove(min_value)
    
    return a

print(custome_sort(array))
print(custome_sort(names))


# T(n) : n*(n+n+n) = n*(3n) = n^2