import random

Chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*-_+='

passlen = input("Please enter the password length: ")
myPass = ''

try:
    while (len(myPass)) <= int(passlen) - 1:
        index = random.randrange(len(Chars))
        myPass = myPass + Chars[index]
        myPassLen = len(myPass)

    print(myPass)

except ValueError:
    print("You have to enter a number, for example: 5")