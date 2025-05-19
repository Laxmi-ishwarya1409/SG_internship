def write():
    text = input("Enter your text:")
    with open("journal_app.txt", "a") as f:
        f.write(text)

    print("Your entry has been saved!\n")



def read():
    try:
        with open("journal_app.txt","r") as f:
            content = f.read()
            print("Your Journal")
            print(content)
    except FileNotFoundError:
        print("No journal found")



def main():
    running= True
    while running:
        print("1. Write new entry")
        print("2. Read all entries")
        print("3. Exit")

        choice = input("Choose an option (1, 2, 3): ")

        if choice == "1":
            write()
        elif choice == "2":
            read()
        elif choice == "3":
            print("Exiting")
            running = False
        else:
            print("Invalid option. Try again.\n")
            running = False

main()