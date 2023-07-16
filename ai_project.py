# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass
    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def create_account(self): 
        #implement function that creates account here
        print("Creating ...")
        name = input("What would you like to set as your name? ")
        age = input("How old are you? ")
        password = input("Please set a password containing at least 4 characters: ")
        if len(password) < 4:
            print("Password is too short. Please input a password that is at least 4 characters long.")
        elif len(password) > 4:
            account = Person(name, age, password)
            self.list_of_people.append(account) #the append function is used to save/upload the inputs into a list (in this case, its uploading to self.list_of_people)
        pass
    #for item in self.list_of_people:
        #if item.id in self.list_of_people:
    def login_account(self):
        if len(self.list_of_people) < 1:
            print("Account not found")
        elif len(self.list_of_people) >=1:
            print(f"The current accounts available to log into are: ")
            for account in self.list_of_people:
                num = 1
                num +=1
                print(account.id)
            accountaccessed = input("Which account would you like to use? Pick a number from the list above. The first account in the list is numbered 0. ")
            accountindex = int(accountaccessed)
            if accountindex in range(len(self.list_of_people)):
                global loginaccount
                loginaccount = self.list_of_people[accountindex]
                print(f"The account you are trying to log into is: {loginaccount.id}")
                confirm = input("Are you sure you want to log into this account? y/n ")
                if confirm == 'y':
                    verify = input("Please input the password of the account you are trying to log into: ")
                    if verify == loginaccount.password:
                        print(f"Verification successful. You are now logged in to: {loginaccount.id}")
                    elif verify != loginaccount.password:
                        print(f"Verification failed. Redirecting back to previous page...")
                if confirm == 'n':
                    print("Login cancelled.")
            elif accountindex not in range(len(self.list_of_people)):
                print("The account you are trying to access is not in the database. Please try again.")
            elif len(self.list_of_people) < 1:
                print("There are no accounts that you can log into. Please create a new account and try again.")
    def getCurrentUser(self):
        username = input("Please input the username associated with your account: ")
        for users in self.list_of_people:
            if users.id == username:
                return users
class Person(SocialNetwork):
    def __init__(self, name, age, password):
        self.id = name
        self.year = age
        self.password = password
        self.friendlist = []
        self.receivedmessages = []
        pass
            #checkforaccount = input("What account would you like to check information for? ")
            #create a program that lets you specify a specific account and then set that account as the variable for current account.
            #currentaccount = 
            
            #print(f"Name: {name} Age: {age} Birthday: {birthday} Email: {email}") #modify this so that it prints out the information for that specific account (ccurrentaccount)
    def add_friend(self, person_object): #previously add_friend(self, person_object)
            for acctid in person_object.list_of_people:
                acctnum = 1
                acctnum +=1
                print("The users that you can currently add as friends are: ", acctid.id)
            yesorno = input("Would you like to add someone as a friend? y/n ")
            if yesorno == 'y':
                userchoice = input("Please input the number of the user you would like to add from the list above. The first account in the list is numbered 0. ")
                friendindex = int(userchoice)
                friend = person_object.list_of_people[friendindex]
                self.friendlist.append(friend)
                print("Friend added!")
            elif yesorno == 'n':
                print("Cancelled. Returning to previous screen.")

        #print("Friend successfuly added.")
        #print(self.friendlist)

        #implement adding friend. Hint add to self.friendlist
            pass
    # def loginAccount(self):
    #     super().__init__() 
    #     if:
    #         print("Account not found")
    #     else:
    #         print("Login successful")
    def check_friends(self):
        if len(self.friendlist) < 1:
            print("There are currently no friended users for this account. Add someone as a friend and try again.")
        elif len(self.friendlist) >=1:
            for accountids in self.friendlist:
                    usernums = 1
                    usernums +=1
                    print("The users that you are currently friends with are: ", accountids.id)
        pass
    def send_message(self, loginaccount):
        if len(self.friendlist) < 1:
            print("There are currently no friended users for this account. Add someone as a friend and try again.")
        elif len(self.friendlist) >=1:
            for accountid in self.friendlist:
                    usernum = 1
                    usernum +=1
                    print("The users that you can currently send messages to are: ", accountid.id)
            friend = input("Who would you like to receive your message? Please input a number. The first account in the list is numbered 0.")
            friendacctnum = int(friend)
            chosenfriend = self.friendlist[friendacctnum]
            sentmessage = input("What message would you like to send? ")
            chosenfriend.receivedmessages.append(loginaccount.id, ": ", sentmessage)
            #self.friendlist[chosenfriend].receivedmessages.append(loginaccount.id, ": ", sentmessage) alternate code for the line shown above
            print(f"Message sent! Receiver: {chosenfriend.id}")
        #put code here in order to send messages to friends and figure out a way to receive messages
        #implement sending message to friend here
    def receive_message(self):
        choice = print("You have a new message! Would you like to check? y/n")
        if choice == 'y':
            print(self.receivedmessages) #have this bit print out the message that was sent previously
        elif choice == 'n':
            print("You have chosen not to check the message. Returning to previous screen.")
        pass
    def item_getName(self):
        return self.id
    def edit_details(self):
        #if account not in self.list_of_people:
            #print("Account not found")
        #else:
        new_age = input("Enter new age: ")
        new_name = input("Enter new name: ")
        self.year = new_age
        self.id = new_name
        passwordver = input("Would you like to change your password? y/n ")
        if passwordver == 'y':
            newpass = input("What would you like your new password to be? ")
            if len(newpass) < 4:
                print("Password is too short. Please input a password with 4 or more characters.")
            elif newpass == loginaccount.password:
                print("Error: Please input a new password.")
            elif len(newpass) > 4:
                newpasscon = ("Please input the new password again to confirm.")
                if newpasscon != newpass:
                    print("Error: the passwords do not match. Please try again.")
                elif newpasscon == newpass:
                    self.password = newpass
                    print(f"Password successfully changed for account: {self.id}")
    def block_user(self):
        s = 1 #placeholder
    def remove_friend(self):
        if len(self.friendlist) >=1:
            for accountids1 in self.friendlist:
                    usernums1 = 1
                    usernums1 +=1
                    print("The users that you are currently friends with are: ", accountids1.id)
        removedfriendname = input("Which friend would you like to remove from the list above? Please select a number. The first name in the list is numbered 0.")
        
# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account") #completed
    print("2. Login to existing account") #completed
    print("3. Manage my account") #in progress
    print("4: Log out of current account") #completed
    print("5. Quit") #completed
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details") #in progress
    print("2. Add a friend") #in progress
    print("3. View all my friends")#in progress
    print("4. View all my messages")#in progress
    print("5: Remove Friend")#in progress
    print("6: Block Friend")#in progress
    print("7: Send Message to Friend")#in progress
    print("8. <- Go back ")
    return input("Please Choose a number: ")

def accountLogin():
    print('')

#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui


#Create instance of main social network object
ai_social_network = SocialNetwork()
loggedoff = True
#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            #ai_social_network.create_account()
            ai_social_network.create_account()
        elif choice == '2':
            inner_menu_choice = social_network_ui.accountLogin()
            ai_social_network.login_account()
            loggedoff = False
            #if
        elif choice == "3":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == '1':
                    if loggedoff == False:
                        currentaccount = ai_social_network.getCurrentUser()
                        currentaccount.edit_details()  #this is still calling the function for a generic person class, link it somehow to the actual account
                    elif loggedoff == True:
                        print("You are not logged into an account. Please log in and try again!")
                        break
                elif inner_menu_choice == '2':
                    if loggedoff == False:
                        currentaccount = ai_social_network.getCurrentUser()
                        currentaccount.add_friend()
                    elif loggedoff == True:
                        print("You are not logged into an account. Please log in and try again!")
                        break
                elif inner_menu_choice == '3':
                    choices = input("Would you like to check your friends list? y/n ")
                    if choices == 'y' and loggedoff == False:
                        currentaccount = ai_social_network.getCurrentUser()
                        currentaccount.check_friends()
                    elif choices == 'n' and loggedoff == True:
                        print("You are not logged into an account. Please log in and try again!")
                        break
                elif inner_menu_choice == '4':
                    if loggedoff == False:
                        currentaccount = ai_social_network.getCurrentUser()
                        currentaccount.receive_message()
                    elif loggedoff == True:
                        print("You are not logged into an account. Please log in and try again!")
                        break
                elif inner_menu_choice == '5':
                    if loggedoff == False:
                        currentaccount = ai_social_network.getCurrentUser()
                        currentaccount.receive_message()
                    elif loggedoff == True:
                        print("You are not logged into an account. Please log in and try again!")
                        break
                elif inner_menu_choice == '6': 
                    if loggedoff == False:
                        s = 1
                    elif loggedoff == True:
                        print("You are not logged into an account. Please log in and try again!")
                        break
                elif inner_menu_choice == '7':
                    if loggedoff == False:
                        loginaccount.send_message(loginaccount)
                    elif loggedoff == True:
                        print("You are not logged into an account. Please log in and try again!")
                        break
                elif inner_menu_choice == "8":
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()
        elif choice == '4':
            print("Account logged out. Please log in again, log into another account, or create a new account.")
            loggedoff = True
        elif choice == "5":
            print("Thank you for visiting. We hope that you visit again soon.")
            break
        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
