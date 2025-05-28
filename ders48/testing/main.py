# def do_stuff(num):
#     return num + 5


# ======================

# 2
# def do_stuff(num):
#     return int(num) + 5

# ======================

# 3 - 4

# def do_stuff(num):
#     try:
#         return int(num) + 5
#     except ValueError as err:
#         return err


# ======================
# 5

def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return "enter a number"
    except ValueError as err:
        return err
