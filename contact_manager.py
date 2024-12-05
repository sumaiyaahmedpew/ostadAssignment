from storage import save_contacts, load_contacts

def add_contact(name, email, phone, address):
    if not name.isalpha():
        print("Error: Name must contain only letters.")
        return
    if not phone.isdigit():
        print("Error: Phone number must be numeric.")
        return

    contacts = load_contacts()
    if any(contact['phone'] == phone for contact in contacts):
        print("Error: Duplicate phone number detected!")
        return

    contact = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address
    }
    contacts.append(contact)
    save_contacts(contacts)

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")

def remove_contact(index):
    contacts = load_contacts()
    if 1 <= index <= len(contacts):
        del contacts[index - 1]
        save_contacts(contacts)
    else:
        print("Error: Invalid index.")

def search_contact(query):
    contacts = load_contacts()
    results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query.lower() in contact['email'].lower() or query.lower() in contact['phone'] or query.lower() in contact['address'].lower()]

    if results:
        print("\nSearch Results:")
        for i, contact in enumerate(results, start=1):
            print(f"{i}. Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.")
