import random

def cekilis(list1:list, list2:list) -> list:
    """
    info: This module draws between two lists
    """
    sonuc = []
    all_in = [list1 ,list2]
    for i in all_in:
        random.shuffle(i)
    for i in zip(list1,list2):
        sonuc.append(i)
    return sonuc
