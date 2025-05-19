# prime number
def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n - 1):
            if n % i == 0:
                return False
        return True

n = int(input("Enter your number: "))

if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")






# reverse a string
def reverse_string(text):
    reversed_str = text[::-1]
    print("Reversed string:", reversed_str)

my_string = input("Enter a string:")
reverse_string(my_string)







# Return the maximum number from a list.
def get_max(numbers):
    if not numbers:
        return None
    else:
        max_value = max(numbers)
        print("Maximum number is:", max_value)

number = input("Enter your input:")
number_list = list(map(float,number.split()))
get_max(number_list)



# Factorial 
def factorial(n):
    if n<0:
        print("Factorial is not defined for negative numbers")
    elif n==0:
        print("1")
    else:
        result = 1
        for i in range(1,n+1):
            result = result * i
        print(f"Factional of {n} :",result)
number = int(input("Enter your number:"))
factorial(number)


# count the words
def count_words(text):
    count = text.split()
    return len(count)

str = input("Enter the text:")
print(count_words(str))