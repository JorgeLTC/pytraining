def add_contact(name: str, phone: str, contacts: dict) -> bool:
    """
    Add a new contact to the contacts dictionary.

    Args:
        name (str): The name of the contact.
        phone (str): The phone number (can contain -, spaces, ., (), etc.).
        contacts (dict[str, str]): The dictionary storing all contacts.

    Returns:
        bool: True if the contact was successfully added, False otherwise.
    """
    # Clean and validate name
    name = name.strip().title()
    if not name:
        print("Error: name can't be empty")
        return False

    # Clean phone number by removing common separators and formatting characters
    raw_phone = (
        phone.replace("-", "")
        .replace(" ", "")
        .replace(".", "")
        .replace("(", "")
        .replace(")", "")
    )

    # Validate phone number: must be exactly 10 digits
    if not raw_phone.isdigit() or len(raw_phone) != 10:
        print("Invalid phone number! must be 10 digits")
        return False

    # Check for duplicate contact
    if name in contacts:
        print(f"Contact '{name}' already exists!")
        return False

    # Format phone number to standard readable format (XXX-XXX-XXXX)
    formatted_phone = f"{raw_phone[:3]}-{raw_phone[3:6]}-{raw_phone[6:]}"

    # Add the contact
    contacts[name] = formatted_phone
    print(f"Contact '{name}' added succesfully!")
    return True


def search_contact(name: str, contacts: dict[str, str]) -> bool:
    """
    Search for a contact by name and display their phone number.

    Args:
        name (str): The name of the contact to search for.
        contacts (dict[str, str]): The dictionary containing all contacts.

    Returns:
        bool: True if the contact was found, False otherwise.
    """
    # Clean the input name the same way we do when adding
    name = name.strip().title()

    if not name:
        print("Error: name can't be empty!")
        return False

    # Search for the contact
    if name in contacts:
        print("\nContact found:")
        print(f"Name: {name}")
        print(f"Phone Number: {contacts[name]}")
        return True
    else:
        print(f"your contact: {name} was not found")
        return False


def display_contacts(contacts: dict[str, str]) -> None:
    """
    Display all saved contacts in a readable format.
    """
    print("\n" + "=" * 40)
    print("          Contacts Available:")
    print("=" * 40)
    if not contacts:
        print("No contacts saved yet")
        print("=" * 40)
        return

    for i, (contact, phone) in enumerate(contacts.items(), 1):
        print(f"{i:2}. {contact:20} → {phone}")
    print("=" * 40)


if __name__ == "__main__":
    contacts = {
        "Juan": "123-321-4567",
        "Robert": "123-321-4568",
        "Jackson": "123-321-4569",
        "Darren": "123-321-4560",
        "Jose": "123-321-4561",
        "Daisy": "123-321-4562",
    }
    while True:
        print("\n" + "=" * 40)
        print("          CONTACT BOOK")
        print("=" * 40)
        print("1 → Add Contact")
        print("2 → Search Contact")
        print("3 → Display All Contacts")
        print("4 → Quit")
        print("=" * 40)

        try:
            choice = int(input("Select your choice: "))
        except ValueError:
            print("please enter a valid number!")
            continue

        match choice:
            case 1:
                name = input("Enter a name: ")
                phone = input("Enter aa phone number: ")
                add_contact(name, phone, contacts)
            case 2:
                name = input("Enter a name: ")
                search_contact(name, contacts)
            case 3:
                display_contacts(contacts)
            case 4:
                print("Bye! Bye!")
                break
            case _:
                print("invalid choice")
