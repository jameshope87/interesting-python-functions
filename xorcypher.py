import random

try:
    input = raw_input
except NameError:
    pass

alphababet = "abcdefghijklmnopqrstuvwxyz"

def take_message():
    message = input('> ')
    return message
    
def encrypt_decrypt(message, key='aaaaa'):
    #assume all same length
    
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(message, key)), key
    
message = take_message()
coded, key = encrypt_decrypt(message)
    
print(coded)
print(key)
