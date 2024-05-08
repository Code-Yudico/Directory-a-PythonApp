#Start menu
names = []
ph_numbers = []
emails = []
print("Hello, welcome to your personal directory, how can I assist you today?")
print("To look for a contact type: search")
print("To add a new contact type: add")
act = input("")

#Search for a contact functionality
if act == "add": 
    name = input("Name:")
    ph_num = input("Phone number:")
    email = input("e-mail:")
    print("Your contact info is:", name, ph_num, email)
    ans1 = input("Do you want to proceed and save the contact? yes/no")
    if ans1 == "yes":
        names.append(name)
        ph_numbers.append(ph_num)
        emails.append(email)
        print("Contact saved")
 #procedure to save the contact here
    else:
        print("Contact not saved")
#Add contact functionality
elif act == "search":
        print("You selected to search for a contact")

#Error at input
else: 
    print("Input not valid, pay attention")