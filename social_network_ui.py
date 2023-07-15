# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Login to existing account")
    print("3. Manage my account")
    print("4. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2: Check current account")
    print("3. Add a friend")
    print("4. View all my friends")
    print("5. View all my messages")
    print("6: Remove Friend")
    print("7: Block Friend")
    print("8. <- Go back ")
    return input("Please Choose a number: ")

def accountLogin():
    print('')
    