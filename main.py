import sys
import contactdb
from datetime import  datetime

def View():
    contactdb.showAllContacts()

def Search():
    print("Enter the first name to search ")
    first_name = input(">>>")
    contactdb.search_contacts(first_name)
    
def Add():
    first_name = input("enter first name\n")
    last_name = input("enter the last name\n")
    nickname = input("enter the nickname\n")
    phone_no = input("enter your phone number\n")
    email_address = input("enter your email address\n")
    time = f"The contact was added on {datetime.now()}"
    if (first_name and last_name and nickname and phone_no and email_address) == "":
        print("Please enter all the fields\n")
    else:
        contactdb.insert_data(first_name,last_name,nickname,phone_no,email_address,time)


def Delete():
    id= input("enter the id of the contact to delete\n")
    contactdb.delete_contact(id)

def main_menu():
    print("1:View")
    print("2:Search")
    print("3:Add")
    print("4:Delete")
    print("5:Quit")



choice = 0
main_menu()
while choice != 5:
    try:
        choice = int(input("Enter your choice(1-5)\n"))
    except:
        print("Enter integers only\n")

    if choice == 1:
        View()

    elif choice == 2:
        Search()
    elif choice == 3:
        Add()
    elif choice == 4:
        Delete()
    elif choice == 5:
        print("Quiting...\n")
        sys.exit()
    else:
        main_menu()
