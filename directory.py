#Start menu
print("Hello, welcome to your personal directory, how can I assist you today?")
print("To look for a contact type: search")
print("To add a new contact type: add")
act = input("")

#Search for a contact functionality
if act == "add": 
    print("You selected to add a contact")

#Add contact functionality
elif act == "search":
        print("You selected to search for a contact")

#Error at input
else: 
    print("Not a valid inpu, pay attention")