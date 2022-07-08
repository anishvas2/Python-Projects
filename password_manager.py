master_password = input("Enter the Master Password: ")

def view():
    with open ('password.txt', 'r') as file:
        for passwords in file.readlines():
            passdata=passwords.rstrip()
            account_name,account_password = passdata.split(":")
            print("User: %s\nPassword: %s"%(account_name,account_password))
def add():

    account_name=input("Enter Website or Account Name: ")
    account_password = input("Enter Password: ")

    with open ('password.txt','a') as file:
        file.write(account_name + ":" + account_password+'\n')

while True:
    choice=input("Want to add or view passwords (Type view or add or exit): ").lower()

    if choice not in ['view','add','exit']:
        continue
    if choice == 'view':
        view()
    elif choice == 'add':
        add()
    elif choice == 'exit':
        break
