import random

Chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*-_+='

passlen = input("Please enter a password lengh: ")
myPass = ''

while (len(myPass)) <= int(passlen) - 1:
        index = random.randrange(len(Chars))
        myPass = myPass + Chars[index]
        myPassLen = len(myPass)

print(myPass)
