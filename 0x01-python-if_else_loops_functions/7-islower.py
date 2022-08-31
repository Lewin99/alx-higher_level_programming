#!/usr/bin/python3
def greetings(c):
    if ord(c) in range(97,124):
        print("lower")
    elif ord(c) in range(65,91):
        print("upper")
     else:
         print("non alphabetic character")
