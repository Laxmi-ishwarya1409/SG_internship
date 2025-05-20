# Create a Employee directory CLI.

def show_options():
        print("Please select the directory:")
        print("1. Add employee")
        print("2. View directory")
        print("3. Search employee")
        print("4. Delete employee")
        print("5. Exit")


def add_emp(directory,emp_id):
    name = input("Enter your name: ")
    department = input("Enter your departmant:")
    email = input("Enter your email:")
    phone_number = input("Enter your phone_number:")
    location = input("Enter your location:")

    for record in directory.values():
        if record["name"] == name:
            print("Employee already exists")
            return emp_id
        

    directory[emp_id] = {
        "name" : name,
        "department" : department,
        "email" : email,
        "phone_number" : phone_number,
        "location" : location
    }
    print(f"Employee {name}, Employee ID {emp_id} added successfully.")
    return emp_id + 1



def view_all_emp(directory):
    if not directory:
        return f"No employees in the directory"
    else:
        print("Employee Directory:")
        for emp_id, info in directory.items():
            print(f"ID: {emp_id}, Name: {info['name']}, Dept: {info['department']}, Email: {info['email']}, Phone: {info['phone_number']}, Location: {info['location']}")

def search_emp(directory):
    emp_id = int(input("Enter the Employee id:"))
    if emp_id in directory:
        info = directory[emp_id]
        print(f"Found: {info}")
    else:
        print("Employee not found.")

def delete_emp(directory):
    emp_id = int(input("Enter employee ID to delete: "))
    if emp_id in directory:
            removed = directory.pop(emp_id)
            print(f"Employee {removed['name']} deleted successfully.")
    else:
        print("Employee not found.")



def main():
    directory = {}
    employee_id = 1

    while True:
        show_options()
        select = input("Enter your choice (1,2,3,4,5): ")

        if select == '1':
            employee_id = add_emp(directory, employee_id)
        elif select == '2':
            view_all_emp(directory)
        elif select == '3':
            search_emp(directory)
        elif select == '4':
            delete_emp(directory)
        elif select == '5':
            print("Exiting...")
            break
        else:
            print("Invalid input, try again...")

main()