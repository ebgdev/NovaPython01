my_list = ["ara", "erfan", "kucuk"]


def reverseStr(astr):
    new_str = ""
    for i in range(len(astr)-1, -1, -1):
        new_str += astr[i]
    return new_str


def isPalindrome(my_list):
    for word in my_list:
        if word == reverseStr(word):
            print(f"{word} is Palindorme")
        else:
            print(f"{word} is Palindorme")


isPalindrome(my_list)
