#Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
#Expected Output :
#60°C is 140 in Fahrenheit
#45°F is 7 in Celsius
num = int(input("Enter your number here:"))
ask = str (input("Do you want to convert it into farenheit or celcius:"))

if ask == str("farenheit"):
    conversion = int((num * 9/5) + 32)
    print (conversion)
elif ask == str("celcius"):
    conversion = int((num - 32) * 5/9)
    print(conversion)