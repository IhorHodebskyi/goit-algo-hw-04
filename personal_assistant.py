from typing import TypedDict
import re




class Contacts(TypedDict):
    name: str
    phone: str


def parse_input(user_input):
    """
    Parse user input into a command and arguments.

    Args:
        user_input (str): The user's input, which may include a command and arguments.

    Returns:
        tuple[str, ...]: A tuple containing the command and any arguments.

    Examples:
        >>> parse_input("hello world")
        ('hello', 'world')
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


     
            
        


def is_valid_contact(contact: Contacts) -> bool:

    """
    Validate a contact dictionary.

    Args:
        contact (Contacts): The contact dictionary to validate.

    Returns:
        bool: True if the contact is valid, False otherwise.

    Notes:
        A contact is considered valid if it has both 'name' and 'phone' keys,
        the 'name' is a non-empty string, and the 'phone' is a 10-digit string.
    """
    if 'name' not in contact or 'phone' not in contact:
        print("Error: Name and phone are required.")
        return False
    

    if not isinstance(contact['name'], str) or len(contact['name']) == 0:
        print("Error: Name should be a non-empty string.")
        return False
    

    if not re.match(r'^\d{10}$', contact['phone']):
        print("Error: Phone number must be 10 digits.")
        return False
    
    return True


def add_contact(value: dict, contacts: list[Contacts]):

    """
    Add a contact to the contacts list.

    Args:
        value (dict): The contact dictionary to add.
        contacts (list[Contacts]): The list of contacts.

    Returns:
        None

    Notes:
        A contact dictionary must have 'name' and 'phone' keys
        and the 'name' must be a non-empty string and the 'phone'
        must be a 10-digit string.
    """
    
    if not is_valid_contact(value):
        print("Contact invalid")

    if value not in contacts:
        contacts.append(value)
        print("Contact added.")
    else:
        print("Contact already exists")
    return    
    



def change_contact(value: dict, contact_list: list[Contacts]):
    """
    Update a contact in the contact list.

    Args:
        value (dict): The contact dictionary with updated information.
        contact_list (list[Contacts]): The list of contacts to search and update.

    Returns:
        None

    Notes:
        The function checks if the provided contact dictionary is valid. If valid,
        it searches for a contact with the same name in the contact list and updates
        it with the new information. If the contact does not exist, a message is printed.
    """

    if not is_valid_contact(value):
        print("Contact invalid")
    
    for i, contact in enumerate(contact_list):
        if contact['name'] == value['name']:
            contact_list[i] = value
            print("Contact updated.")
            return
    print("Contact not found.")

def show_phone(name: str, contact_list: list[Contacts]):

    """
    Print the phone number of a contact.

    Args:
        name (str): The name of the contact to search for.
        contact_list (list[Contacts]): The list of contacts to search in.

    Returns:
        None

    Notes:
        If the contact is not found, a message is printed.
    """
    if name not in contact_list:
        print("Contact not found.")
    else:
        for contact in contact_list:
            if contact['name'] == name:
                print(f"Phone number for {name}: {contact['phone']}")
                return

def show_all(contacts: list[Contacts]):
    for item in contacts:
        print(f"name: {item["name"]} phone: {item["phone"]}", end="")



def main():
    """
    Main function for the personal assistant bot.

    This function prints a welcome message, then enters a loop where it prompts the user for a command.
    The commands are:

    - add <name> <phone>: Adds a contact with the given name and phone number.
    - change <name> <phone>: Changes the phone number of the contact with the given name.
    - phone <name>: Prints the phone number of the contact with the given name.
    - all: Prints all the contacts.
    - hello: Prints a greeting message.
    - close/exit: Exits the loop and ends the program.

    If the user enters an invalid command, the program prints an error message.
    """
    print("Welcome to the assistant bot!")
    contacts = []

    while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)


            if command in ["close", "exit"]:
                print("Good bye!")
                break

     
            if "add" == command:
                if len(args) == 2:
                    add_contact({"name": args[0], "phone": args[1]}, contacts)
                    print(contacts)
                else:
                    print("Insufficient information to add contact.")
            elif "change" == command:
                if len(args) == 2:
                    change_contact({"name": args[0], "phone": args[1]}, contacts)
                    print(contacts)
                else:
                    print("Insufficient information to change contact.")
            elif "phone" == command:
                if len(args) == 1:
                    show_phone(args[0], contacts)
                else:
                    print("There is not enough information to display the number.")
            elif "all" == command:
                show_all(contacts)
            elif "hello"  == command:
                print("How can I help you?")
            else:
                print("Invalid command.")


if __name__ == "__main__":

    main()