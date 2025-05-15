# Create a program to calculate grades based on input scores.


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



# Build a decision-making application using complex conditional logic.
# loan eligibility checker

age = int(input("Enter your age: "))
income = int(input("Enter your Income : "))
employment_status = input("Enter your employment status: ").lower()
credit_score = int(input("Enter your credit score: "))
has_existing_loan = input("Do you have any existing loan? (yes/no): ").lower()


if age < 21 :
    print("Not Eligible: Age should be above 21")

elif income < 25000 or employment_status == "unemployed":
    print("Not eligible: Employment is needed or income should be above 25000 ")

elif credit_score < 650:
    print("Not eligible: Credit score is too low (minimum 650 required).")


else:
    if has_existing_loan == "yes":
        print("Existing loan found: You may have limited eligibility.")
    else:
        print(" Approved: You are eligible for the loan")


# message = "Existing loan found: You may have limited eligibility." if has_existing_loan == "yes" else "Approved: You are eligible for the loan"
# print(message)