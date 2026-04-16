def add_contact(contact_list):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contact = name + " - " + phone
    contact_list.append(contact)
    print("Contact added successfully!")

def show_contacts(contact_list):
    if len(contact_list) == 0:
        print("No contacts yet")
    else:
        print("\n--- Contact List ---")
        for i in range(len(contact_list)):
            print(f"{i+1}. {contact_list[i]}")

def search_contact(contact_list):
    name = input("Enter name to search: ")
    found = False
    for contact in contact_list:
        if name.lower() in contact.lower():
            print("Found:", contact)
            found = True
    if not found:
        print("Not found")

def main():
    my_contacts = []

    while True:
        print("\n=== CONTACT MANAGEMENT SYSTEM ===")
        print("1. Add new contact")
        print("2. Display all contacts")
        print("3. Search contact")
        print("4. Exit program")
        print("=================================")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_contact(my_contacts)
        elif choice == '2':
            show_contacts(my_contacts)
        elif choice == '3':
            search_contact(my_contacts)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()