num = int(input("Your number :"))
num2 = num
space = " "
con =int(input("You want to convert in octal(8) or binary(2) or hexadecimal(16) :"))

while num2 != 0 :
    rem = num2 % con
    if rem == 10 :
        rem = "A"
    elif rem == 11 :
        rem = "B"
    elif rem == 12 :
        rem = "C"
    elif rem == 13 :
        rem = "D" 
    elif rem == 14 :
        rem = "E" 
    elif rem == 15 :
        rem = "F"
    space = str(rem) + space
    num2 = int(num2 / con) 

print(space) 
