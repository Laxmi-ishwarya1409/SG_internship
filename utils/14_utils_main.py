from utils.util_functions import is_prime, reverse_string, get_max, factorial, count_words

n = int(input("Enter a number: "))
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")




my_string = input("Enter a string: ")
print("Reversed string:", reverse_string(my_string))




number = input("Enter numbers separated by space: ")
number_list = list(map(float, number.split()))
print("Maximum number is:", get_max(number_list))




number = int(input("Enter number for factorial: "))
fact = factorial(number)
if fact is None:
    print("Factorial not defined for negative numbers.")
else:
    print(f"Factorial of {number}: {fact}")





input_str = input("Enter a text: ")
print("Word count:", count_words(input_str))