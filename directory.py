class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def __str__(self):
        return f"""
        Name: {self.name}
        Phone: {self.phone}
        Email: {self.email}
        """

class ContactList:
    contacts = []
    def __str__(self):
        return str([str(contact) for contact in self.contacts])
    def addContact(self,contact):
        self.contacts.append(contact)

contactList = ContactList()

paco = Contact("Paco", "5564554", "paco@gmail")

contactList.addContact(paco)


ana = Contact("Ana", "55454", "qnq@gmail.com")
contactList.addContact(ana)
print(paco.email)