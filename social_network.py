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
            #ai_social_network.create_account()
            ai_social_network.create_account()
        elif choice == '2':
            inner_menu_choice = social_network_ui.accountLogin()
            #insert choice here
            ai_social_network.login_account()
            #if
        elif choice == "3":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == '1':
                    name = input("What is the name of the account you are editing? ")
                    name.edit_details()  #this is still calling the function for a generic person class, link it somehow to the actual account
                elif inner_menu_choice == '2':
                    loginaccount.add_friend()
                elif inner_menu_choice == '3':
                    choices = input("Would you like to check your friends list? y/n ")
                    if choices == 'y':
                        Person.check_friends()
                    else:
                        inner_menu_choice = social_network_ui.manageAccountMenu()
                elif inner_menu_choice == '4':
                    s = 1
                elif inner_menu_choice == '5':
                    s = 1
                elif inner_menu_choice == '6': 
                    s = 1
                elif inner_menu_choice == "7":
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()
        elif choice == '4':
            print("Account logged out. Please log in again, log into another account, or create a new account.")
        elif choice == "5":
            print("Thank you for visiting. Goodbye3")
            break
        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
