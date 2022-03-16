from msilib.schema import Binary


num = int(input("Enter your number \n->"))
decimal = num
while decimal!=0:
    updater= int(decimal%2)
    decimal = decimal/2
    decimal = str(updater)+updater

print(decimal)


 


