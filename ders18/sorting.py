my_arr = ["fatih","adil","taha","meserret"]

def sorting(lst):
    sorted_array = [] # adil,fatih,meserret,taha

    for name in lst: # name = meserret
        flag = False
        for i in range(len(sorted_array)):
            if name < sorted_array[i]:
                sorted_array.insert(i,name)
                flag = True
                break
        if flag == False:
            sorted_array.append(name)
    return sorted_array

print(sorting(my_arr))


