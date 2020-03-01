import random

Chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*-_+='

passLen = 26
myPass = ''

for i in range(passLen):
    while (len(myPass)) <= 25:
        index = random.randrange(len(Chars))
        myPass = myPass + Chars[index]
        myPassLen = len(myPass)

print(myPass)
