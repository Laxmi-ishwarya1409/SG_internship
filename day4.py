my_number = 42

while True:
    guess_number = int(input("Enter the number: "))

    if guess_number > my_number:
        print("Too high")

    elif guess_number < my_number:
        print("Too low")

    else:
        print("Correct")
        break



my_number = 42
guess_number = int(input("Enter the number: "))
while guess_number != my_number:
    if guess_number > my_number:
        print("Too high")
    else:
        print("Too low")
    
    guess_number = int(input("Try again: "))
print("Correct!")








my_number = 42
maximum_attempts = 3 

for attempt in range(1,  maximum_attempts + 1):
    guess_number = int(input(f"Attempt {attempt}/{ maximum_attempts}: Enter your guess: "))

    if guess_number > my_number:
        print("Too high")
    elif guess_number < my_number:
        print("Too low")
    else:
        print("Correct")
        break 

else:
    print(f"You've used all {maximum_attempts} attempts. The secret number was {my_number}.")


# Create pattern-printing programs using nested loops.

# grid
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

# right angle 
for i in range(1, 6): 
    for j in range(i):  #the number of stars equals the row number
        print("*", end="")  
    print()  

# pyramid
for i in range(1, 6):  
    for j in range(5 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")  
    print()

# inverted triangle
for i in range(5, 0):  
    for j in range(i):  
        print("*", end="")  
    print()