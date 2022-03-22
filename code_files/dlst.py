#Difference between 
#List - square braces Mutable - can change
#Tuple - rounded braces    IMMUTABLE- cannot change item
#Set -  the set keyword
#Dictionary - 

list1 = ['Computer','Printer','TV']
list1[0] = "pc"
print(list1) # changing the value inside 
tuple1 =  ('Computer','Printer','TV')
print(tuple1)

print(list1)

dict1 = { 
        "1":"Monday",
        "2" :"tuesday",
        "3" : "Wednesday"
        }
for n in dict1["1"] :
    print(n)
