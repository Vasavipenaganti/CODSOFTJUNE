class Contact:
    def _init_(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class AddressBook:
    def _init_(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, index, new_name, new_phone, new_email, new_address):
        contact = self.contacts[index]
        contact.name = new_name
        contact.phone = new_phone
        contact.email = new_email
        contact.address = new_address

    def delete_contact(self, index):
        del self.contacts[index]

def display_contact(contact):
    print(f"Name: {contact.name}")
    print(f"Phone: {contact.phone}")
    print(f"Email: {contact.email}")
    print(f"Address: {contact.address}")

def main():
    address_book = AddressBook()

    while True:
        print("\n--- Address Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            address_book.add_contact(contact)
            print("Contact added successfully!")

        elif choice == '2':
            address_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = address_book.search_contact(keyword)
            if not results:
                print("No matching contacts found.")
            else:
                print("Matching Contacts:")
                for i, contact in enumerate(results, 1):
                    print(f"{i}. Name: {contact.name}, Phone: {contact.phone}")

        elif choice == '4':
            index = int(input("Enter the index of the contact to update: ")) - 1
            if 0 <= index < len(address_book.contacts):
                new_name = input("Enter new name: ")
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email: ")
                new_address = input("Enter new address: ")
                address_book.update_contact(index, new_name, new_phone, new_email, new_address)
                print("Contact updated successfully!")
            else:
                print("Invalid index.")

        elif choice == '5':
            index = int(input("Enter the index of the contact to delete: ")) - 1
            if 0 <= index < len(address_book.contacts):
                del_contact = address_book.contacts[index]
                address_book.delete_contact(index)
                print(f"{del_contact.name} deleted from contacts.")
            else:
                print("Invalid index.")

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
