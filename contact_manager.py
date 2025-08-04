import json

FILENAME = "contacts.json"

# --- Load contacts from file ---
def load_contacts():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # return empty list if file doesn't exist or is empty

# --- Save contacts to file ---
def save_contacts(contacts):
    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent=4)

# --- Add contact ---
def add_contact(name, number, email):
    contacts = load_contacts()
    contacts.append({"name": name, "number": number, "email": email})
    save_contacts(contacts)
    print("Contact added successfully.")

# --- View all contacts ---
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Number: {contact['number']}, Email: {contact['email']}")

# --- Update contact ---
def update_contact(index, name=None, number=None, email=None):
    contacts = load_contacts()
    if 0 <= index-1 < len(contacts):
        if name:
            contacts[index-1]["name"] = name
        if number:
            contacts[index-1]["number"] = number
        if email:
            contacts[index-1]["email"] = email
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Invalid contact number.")

# --- Delete contact ---
def delete_contact(index):
    contacts = load_contacts()
    if 0 <= index-1 < len(contacts):
        removed = contacts.pop(index-1)
        save_contacts(contacts)
        print(f"Deleted contact: {removed['name']}")
    else:
        print("Invalid contact number.")
