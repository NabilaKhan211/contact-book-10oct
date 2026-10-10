# Veda Technology Python Internship - Day 10
# Simple contact book = add , view , search , update and delete

"""Command-line Contact Book built with Python dictionaries.

Data model (key-value pairs):
    contacts = {
        "9876543210": {"name": "Aarav Sharma", "email": "aarav@example.com", "city": "Bhopal"},
        ...
    }
The phone number is the unique key, so duplicates are easy to detect.
"""

# ---------- Sample data ----------
contacts = {
    "9876543210": {"name": "Aarav Sharma", "email": "aarav@example.com", "city": "Bhopal"},
    "9123456780": {"name": "Priya Verma", "email": "priya@example.com", "city": "Indore"},
    "9988776655": {"name": "Rahul Khan", "email": "rahul@example.com", "city": "Delhi"},
    "9090909090": {"name": "Sneha Patel", "email": "sneha@example.com", "city": "Mumbai"},
}


# ---------- Validation helpers ----------
def is_valid_phone(phone):
    """A valid phone is exactly 10 digits."""
    return phone.isdigit() and len(phone) == 10


def is_valid_email(email):
    """Very simple check: something@something.something (or blank)."""
    if email == "":
        return True
    return "@" in email and "." in email.split("@")[-1] and " " not in email


def ask_phone(prompt="Enter phone number (10 digits): "):
    phone = input(prompt).strip()
    if not is_valid_phone(phone):
        print("Invalid phone number. It must be exactly 10 digits.")
        return None
    return phone


# ---------- CRUD operations ----------
def add_contact():
    """CREATE: add a new contact, rejecting duplicate phone numbers."""
    phone = ask_phone()
    if phone is None:
        return
    if phone in contacts:
        print(f"Duplicate entry: {phone} already belongs to {contacts[phone]['name']}.")
        return
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    email = input("Enter email (optional): ").strip()
    if not is_valid_email(email):
        print("Invalid email format.")
        return
    city = input("Enter city (optional): ").strip()
    contacts[phone] = {"name": name, "email": email, "city": city}
    print(f"Contact '{name}' added successfully.")


def view_contacts():
    """READ: list all contacts in a table, sorted by name."""
    if not contacts:
        print("Contact book is empty.")
        return
    print(f"\n{'Phone':<12} {'Name':<20} {'Email':<25} {'City':<12}")
    print("-" * 71)
    for phone, info in sorted(contacts.items(), key=lambda item: item[1]["name"].lower()):
        print(f"{phone:<12} {info['name']:<20} {info['email']:<25} {info['city']:<12}")
    print(f"\nTotal contacts: {len(contacts)}")


def search_contact():
    """READ: search by phone (exact) or by name (partial, case-insensitive)."""
    term = input("Enter name or phone to search: ").strip().lower()
    if not term:
        print("Search term cannot be empty.")
        return
    matches = {
        phone: info for phone, info in contacts.items()
        if term == phone or term in info["name"].lower()
    }
    if not matches:
        print("No contact found.")
        return
    print(f"\nFound {len(matches)} contact(s):")
    for phone, info in matches.items():
        print(f"  {phone} | {info['name']} | {info['email']} | {info['city']}")


def update_contact():
    """UPDATE: change fields of an existing contact (press Enter to keep a value)."""
    phone = ask_phone("Enter phone number of contact to update: ")
    if phone is None:
        return
    if phone not in contacts:
        print("Contact not found.")
        return
    info = contacts[phone]
    print(f"Updating {info['name']} (press Enter to keep current value)")
    name = input(f"Name [{info['name']}]: ").strip()
    email = input(f"Email [{info['email']}]: ").strip()
    city = input(f"City [{info['city']}]: ").strip()
    if email and not is_valid_email(email):
        print("Invalid email format. Update cancelled.")
        return
    if name:
        info["name"] = name
    if email:
        info["email"] = email
    if city:
        info["city"] = city
    print("Contact updated successfully.")


def delete_contact():
    """DELETE: remove a contact after confirmation."""
    phone = ask_phone("Enter phone number of contact to delete: ")
    if phone is None:
        return
    if phone not in contacts:
        print("Contact not found.")
        return
    confirm = input(f"Delete {contacts[phone]['name']}? (y/n): ").strip().lower()
    if confirm == "y":
        del contacts[phone]
        print("Contact deleted.")
    else:
        print("Deletion cancelled.")


# ---------- Menu ----------
MENU = """
========== CONTACT BOOK ==========
1. Add contact
2. View all contacts
3. Search contact
4. Update contact
5. Delete contact
6. Exit
==================================
"""

ACTIONS = {
    "1": add_contact,
    "2": view_contacts,
    "3": search_contact,
    "4": update_contact,
    "5": delete_contact,
}


def main():
    while True:
        print(MENU)
        choice = input("Choose an option (1-6): ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        action = ACTIONS.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()