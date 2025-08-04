import contact_manager as cm

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        email = input("Enter email: ")
        cm.add_contact(name, number, email)

    elif choice == "2":
        cm.view_contacts()

    elif choice == "3":
        cm.view_contacts()
        index = int(input("Enter contact number to update: "))
        name = input("Enter new name (or press Enter to skip): ")
        number = input("Enter new number (or press Enter to skip): ")
        email = input("Enter new email (or press Enter to skip): ")
        cm.update_contact(index, name if name else None, number if number else None, email if email else None)

    elif choice == "4":
        cm.view_contacts()
        index = int(input("Enter contact number to delete: "))
        cm.delete_contact(index)

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
