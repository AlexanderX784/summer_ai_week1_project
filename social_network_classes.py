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
        self.list_of_people.append(Person(name, age, birthday)) #the append function is used to save/upload the inputs into a list (in this case, its uploading to self.list_of_people)
        pass
    

    #for item in self.list_of_people:
        #if item.id in self.list_of_people:


class Person(SocialNetwork):
    def __init__(self, name, age, birthday):
        self.id = name
        self.year = age
        self.birthday = birthday
        self.friendlist = []
        pass
    def check_account(self):
        super().__init__()
        person1 = Person(self.id, self.year, self.birthday)
        if person1 not in self.list_of_people:
            print("Account not found")
        else:
            #checkforaccount = input("What account would you like to check information for? ")
            #create a program that lets you specify a specific account and then set that account as the variable for current account.
            #currentaccount = 
            print(f"Your current account is: {self.id}")
            #print(f"Name: {name} Age: {age} Birthday: {birthday} Email: {email}") #modify this so that it prints out the information for that specific account (ccurrentaccount)
    def add_friend(self, person_object):
        person_object = input("Please input the username of the friend you would like to add: ")
        self.friendlist.append(person_object)
        #implement adding friend. Hint add to self.friendlist
        pass
    def loginAccount():
        super().__init__()
        thing = input("Please input the name of the account you want to log into: ")
        #if thing not in self.list_of_people:
            #print("Account not found")
        #else:
    def check_friends(self):
        print(self.friendlist) 
        pass
    def send_message(self):
        message = input("What message would you like to send? ")
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

        
