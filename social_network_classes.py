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
        birthday = input("When is your birthday? ")
        account = Person(name, age, birthday)
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
                loginaccount = self.list_of_people[accountindex]
                print(f"The account you are trying to log into is: {loginaccount.id}")
                confirm = input("Are you sure you want to log into this account? y/n ")
                if confirm == 'y':
                    print(f"Login successful! The account you are currently logged into is: {loginaccount.id}")
                if confirm == 'n':
                    print("Login cancelled.")
            elif accountindex not in range(len(self.list_of_people)):
                print("The account you are trying to access is not in the database. Please try again.")
            elif len(self.list_of_people) < 1:
                print("There are no accounts that you can log into. Please create a new account and try again.")
class Person(SocialNetwork):
    def __init__(self, name, age, birthday):
        self.id = name
        self.year = age
        self.birthday = birthday
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
        print(self.friendlist) 
        pass
    def send_message(self):
        message = input("What message would you like to send? ")
        print("The users that you can currently send messages to are: ")

        #put code here in order to send messages to friends and figure out a way to receive messages
        #implement sending message to friend here
    def receive_message(self):
        print() #have this bit print out the message that was sent previously
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