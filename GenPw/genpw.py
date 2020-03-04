import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*-_+='
mypass = ''
check = 0

while check == 0:
    passlen = input("Please enter the password length: ")
    try:
        while (len(mypass)) <= int(passlen) - 1:
            index = random.randrange(len(chars))
            mypass = mypass + chars[index]
            mypassLen = len(mypass)
        print(mypass)
        check = 1
    except ValueError:
        print("You have to enter a number, for example: 5")