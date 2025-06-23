# prime number
def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n - 1):
            if n % i == 0:
                return False
        return True


# reverse a string
def reverse_string(text):
    reversed_str = text[::-1]


# Return the maximum number from a list.
def get_max(numbers):
    if not numbers:
        return None
    else:
        max_value = max(numbers)
        print("Maximum number is:", max_value)



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

# count the words
def count_words(text):
    count = text.split()
    return len(count)