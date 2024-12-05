from contact_manager import add_contact, view_contacts, remove_contact, search_contact

def main():
    while True:
        print("\nWelcome to Contact Book Management System:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone Number: ")
            address = input("Enter Address: ")
            add_contact(name, email, phone, address)
            print("Contact added successfully!")
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            index = int(input("Enter the index of the contact to remove: "))
            remove_contact(index)
            print("Contact removed successfully!")
        elif choice == "4":
            query = input("Enter search query: ")
            search_contact(query)
        elif choice == "5":
            print("Exiting Contact Book Management System...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
