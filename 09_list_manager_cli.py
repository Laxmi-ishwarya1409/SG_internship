# Create a CLI to-do list manager.

tasks = []

while True:
    print("Please select the task:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    select = input("Enter your choice (1,2,3,4): ")

    if select == '1':
        add_task = input("Enter your task: ")
        completed = False
        for task in tasks:
            if task[0] == add_task:
                print("Task already exists...")
                break
        else:
            tasks.append((add_task, completed))
            print(f"Task {add_task} added successfully.")

    elif select == '2':
        if not tasks:
            print("No tasks available")
        else:
            print("Tasks:")
            for i in range(0, len(tasks)):
                task, completed = tasks[i]
                status = "Completed" if completed else "Not Completed"
                print(f"{i + 1}.{task} (Status: {status})")

    elif select == '3':
        try:
            task_num = int(input("Enter your task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task {removed_task[0]} removed successfully")
            else:
                print("Invalid Task Number")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif select == '4':
        print("Exiting...")
        break

    else:
        print("Invalid input, try again...")
