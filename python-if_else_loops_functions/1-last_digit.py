#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last digit = abs( number%10)
if Last digit > 5:
    print("Last digit of",number "is",Last digit,"and" number "is greater than 5")
elif Last digit < 6 
    print("Last digit of",number "is",Last digit,"and" number "is less than 6")
else:
    print(""Last digit of",number "is",Last digit,"and" number "is equal to 0"
