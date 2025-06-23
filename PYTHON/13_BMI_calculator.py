# Create a BMI calculator function.
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / height_m ** 2

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi_value, bmi_category = calculate_bmi(weight, height)

print(f"\nYour BMI is: {bmi_value:.2f}")
print(f"You are classified as: {bmi_category}")