# Create a simple calculator that performs addition, subtraction, multiplication, and division.



class StrError(Exception):
   pass


def calculator():
    running = True
    while running:
        try:
            print("Please select the operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")

            select = input("Enter your selection (1, 2, 3, 4, 5): ").strip()

            if select not in ['1', '2', '3', '4', '5']:
                raise ValueError("Invalid operation selected.")

            if select in ['1', '2', '3', '4']:
                num1 = (input("Enter the first number: "))
                num2 = (input("Enter the second number: "))
                
                if not isinstance(num1,int):
                    raise StrError("the input is not int")


                if select == '1':
                    result = num1 + num2
                    operation = "Addition"
                elif select == '2':
                    result = num1 - num2
                    operation = "Subtraction"
                elif select == '3':
                    result = num1 * num2
                    operation = "Multiplication"
                elif select == '4':
                    if num2 == 0:
                        raise ZeroDivisionError("Cannot divide by zero.")
                    result = num1 / num2
                    operation = "Division"

                print(f"{operation} result is: {result}")

            if select == '5':
                print("Exiting")
                running = False

        except ValueError as ve:
            print("Input Error:", ve)

        except Exception as e:
            print("Something went wrong:", e)

calculator()