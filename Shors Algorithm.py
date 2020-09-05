import math
import random

def GCD(a,b):
    r = 1
    q = 0
    if a > b :
        while r != 0:
            r = a % b
            q = math.floor(a / b)
            a = b
            b = r
        return a
    else:
        while r != 0:
            r = b % a
            q = math.floor(b / a)
            b = a
            a = r
        return b



number = int(input("Enter the number of which prime factors you need"))

def Shors(number):
    m = random.randrange(1,number,1)
    d = 0
    i = 1
    if GCD(number , m) == 1:
        while d != 1:
            d = (m**i) % number
            i = i + 1
        if i % 2 == 0 and (((m**(i/2)) + 1) % number != 0):
            print(GCD(((m**(i/2))+1),number),",",GCD(((m**(i/2))-1),number))
        else:
            Shors(number)
    else:
        Shors(number)

Shors(number)