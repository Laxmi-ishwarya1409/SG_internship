# Build a contact book using dictionaries.
def contact_book():
    contact_book = {}
    running = True

    while running:
        print("Contact Book:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Exit")

        select = input("Enter the operation(1,2,3,4,5):")

        if select == "1":
            add_name = input("Enter your name: ")
            add_num = input("Enter your phone number: ")

            if add_num in contact_book.values():
                print("Contact already exists.")
            else:
                contact_book[add_name] = add_num
                print("Contact added successfully!")

        elif select == "2":
            if not contact_book:
                print("No Contacts available")
            else:
                print("Available contact")
                # print(contact_book)
                for name, number in contact_book.items():
                    print(f"{name} - {number}")


        elif select == "3":
            remove_contact = input("Enter the name to remove:")
            if remove_contact in contact_book.keys():
                contact_book.pop(remove_contact)
                print(f"{remove_contact} has removed succesfully")
            else:
                print("Cannot find the contact")

        elif select == "4":
            search_contact = input("Enter the name to search:")
            if search_contact in contact_book:
                # print(contact_book["search_contact"])
                print(contact_book.get(search_contact))

            else:
                print("Not found")

        elif select == "5":
            print("Exiting")
            running = False

        else:
            print("Invalid input")
            running = False

contact_book()