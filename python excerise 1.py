#Question 1:Variable Assignment and String Manipulation
name = input("My name is: ")
print(name)
age = input("Please enter your age: ")
print("Hello Mr, "+name+ age)

#Question 2: Integer Operation
length = int(input("Enter the length of the rectangle: "))
width =int(input("Enter the width of the rectangle: "))
area = length * width
print("area: " , + area)

#Question 3: Working with Floats
Celsius = float(input("What is the weather in celsius: "))
user_tempreture = Celsius
Fahrenheit = (Celsius * 9/5) + 32
print(f"The Fahrenheit is {round(Fahrenheit, 2)}")