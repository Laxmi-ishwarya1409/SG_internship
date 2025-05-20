# Create a program to calculate grades based on input scores.
def grade_calculator():
    try:
        score = int(input("Enter your score: "))

        if score < 0 or score > 100:
            print("Invalid input. Score must be between 0 and 100")
        elif score > 85:
            print("Grade: A - Excellent")
        elif score > 65:
            print("Grade: B - Good")
        elif score > 45:
            print("Grade: C - Just passed")
        else:
            print("Fail!")

    except ValueError as ve:
        print("Input Error:", ve)

    except Exception as e:
            print("Something went wrong:", e)

grade_calculator()