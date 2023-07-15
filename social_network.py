#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()

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
            ai_social_network.create_account()
        elif choice == '2':
            inner_menu_choice = social_network_ui.accountLogin()
            #insert choice here
            account1 = input("Please input the name of the account you are trying to log into: ")
            account1.loginAccount()
            #if
        elif choice == "3":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == '1':
                    name = input("What is the name of the account you are editing? ")
                    name.edit_details()  #this is still calling the function for a generic person class, link it somehow to the actual account
                elif inner_menu_choice == '2':
                    myaccount = input("Do you want to check the current account? y/n ")
                    if myaccount == 'y':
                        name1 = input("What is the name of the account? ")
                        age1 = input("How old are you? ")
                        birthday1 = input("When is your birthday? ")
                        name2 = Person(name1, age1, birthday1)
                        name2.check_account()
                    elif myaccount == 'n':
                        inner_menu_choice = social_network_ui.manageAccountMenu()
                    else:
                        inner_menu_choice = social_network_ui.manageAccountMenu()
                elif inner_menu_choice == '3':
                    Person.add_friend()
                elif inner_menu_choice == '4':
                    Person.check_friends()
                elif inner_menu_choice == '5':
                    s = 1
                elif inner_menu_choice == '6':
                    s = 1
                elif inner_menu_choice == '7': 
                    s = 1
                elif inner_menu_choice == "8":
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()
        elif choice == "4":
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
