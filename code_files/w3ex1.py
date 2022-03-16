#1. Write a Python program to find 
# those numbers which are divisible 
# by 7 and multiple of 5, between 1500 
# and 2700 (both included).
#https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
num = int(input("Enter your number\n->"))
while num<1500 or num>2700:
    print("You num should be between 1500 and 2700 ")
    num = int(input("Enter your number\n->"))
check1 = num % 7
check2 = num % 5

if check1 == 0 :
    print(f"{num} is divisible by 7.")
elif check1 != 0 :
     print(f"{num} isn't divisible by 7.")

if check2 == 0 :
    print(f"{num} is a multiple of 5.")
elif check2 != 0 :
    nprint (f"{num} isn't divisible by 5.)
