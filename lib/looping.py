#!/usr/bin/env python3

def happy_new_year():
     i = 10
while i > 0:
        print(i)
        i -= 1
print("Happy New Year!")

def square_integers(int_list):
    return [int * int for int in int_list]

def fizzbuzz():
    x = 1
    while x < 101:
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)
        x += 1 
