import random

Chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*-_+='
myPass = ''
check = 0

while check == 0:
    passlen = input("Please enter the password length: ")
    try:
        while (len(myPass)) <= int(passlen) - 1:
            index = random.randrange(len(Chars))
            myPass = myPass + Chars[index]
            myPassLen = len(myPass)
        print(myPass)
        check = 1
    except ValueError:
        print("You have to enter a number, for example: 5")