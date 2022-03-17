num = int(input("Enter your number here \n->"))
quo  = num
binary = ""

while quo != 0 :
    
    rem = quo % 2
    binary = str(rem) + binary
    quo = int(quo /2) 

print(f"{num} in binary is {binary}.")
