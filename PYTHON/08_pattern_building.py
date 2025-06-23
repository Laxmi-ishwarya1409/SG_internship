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