# Create a simple calculator that performs addition, subtraction, multiplication, and division.

print("Please select the operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

select = input("Enter your select (1,2,3,4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if select == '1':
    print(f"Result: {num1 + num2}")
elif select == '2':
    print(f"Result: {num1 - num2}")
elif select == '3':
    print(f"Result: {num1 * num2}")
elif select == '4':
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid input")















def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    num1 - num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1 / num2

print("Please select the operation:\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division")


select = int(input("Select an operation from 1,2,3,4: "))

number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))


if select == 1:
    print("Addition of two number is:",add(number1,number2))

elif select == 2:
    print("Subtraction of two number is:",sub(number1,number2))

elif select == 3:
    print("Multiplication of two number is:",mul(number1,number2))

elif select == 4:
    if number2 != 0:
        print("Division of two number is:",div(number1,number2))
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid Operation")

# Experiment with different data types and conversions.

x = 1
y = 1.456
z = complex(5,9)
z1 = complex(5,9.258)
p = "123"
p1 = "ish"


a = float(x)
b = int(y)
# b1 = int(z)     # int() argument must be a string, a bytes-like object or a real number, not 'complex'
d = complex(y)
b2 = int(p)
a1 = float(p)
# c = int(p1)   # int() argument must be a string, a bytes-like object or a real number, not 'complex'
f = str(y)



print(type(a))
print(type(b))
print(type(d))
print(type(b2))
print(type(a1))
print(type(f))