user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    # code here
    pass

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)

