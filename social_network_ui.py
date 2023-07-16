# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account") #completed
    print("2. Login to existing account") #completed
    print("3. Manage my account")
    print("4: Log out of current account")
    print("5. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5: Remove Friend")
    print("6: Block Friend")
    print("7. <- Go back ")
    return input("Please Choose a number: ")

def accountLogin():
    print('')
    