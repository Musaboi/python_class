num1 = int(input("Highest number: "))
num2 = int (input("Lowest number: "))
list = [num1, num2]
for elements in range(list[0],list[1],-1):
    print(elements)