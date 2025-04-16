adict = {"10001":{"name":"adil","age":28}}
bdict = {"10002":{"name":"taha","age":20}}



def merge_dicts(a,b):
    a.update(b)
    return a


print(merge_dicts(adict,bdict))