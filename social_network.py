# import json
# from  social_network_classes import SocialNetwork,Person
# import social_network_ui
# ai_social_network = SocialNetwork()
# loggedoff = True
# #The line below is a python keyword to specify which 
# if __name__ == "__main__":
#     print("########################################################")
#     print("          Welcome to Summer AI Social Network")
#     print("########################################################")
#     last_menu = None
#     choice = social_network_ui.mainMenu()
    

#     while True: 


#         if choice == "1":
#             print("\nYou are now in the create account menu")
#             #ai_social_network.create_account()
#             ai_social_network.create_account()
#         elif choice == '2':
#             inner_menu_choice = social_network_ui.accountLogin()
#             ai_social_network.login_account()
#             loggedoff = False
#             #if
#         elif choice == "3":
#             inner_menu_choice = social_network_ui.manageAccountMenu()
#             #Handle inner menu here
#             while True:
#                 if inner_menu_choice == '1':
#                     if loggedoff == False:
#                         loginaccount.edit_details()  #this is still calling the function for a generic person class, link it somehow to the actual account
#                         inner_menu_choice = social_network_ui.manageAccountMenu()
#                     elif loggedoff == True:
#                         print("You are not logged into an account. Please log in and try again!")
#                         break
#                 elif inner_menu_choice == '2':
#                     if loggedoff == False:
#                         loginaccount.add_friend(ai_social_network)
#                         break
#                     elif loggedoff == True:
#                         print("You are not logged into an account. Please log in and try again!")
#                         break
#                 elif inner_menu_choice == '3':
#                     choices = input("Would you like to check your friends list? y/n ")
#                     if loggedoff == True:
#                         print("You are not logged into an account. Please log in and try again.")
#                     if loggedoff == False:
#                         if choices == 'y':
#                             loginaccount.check_friends()
#                         elif choices == 'n':
#                             break
#                 elif inner_menu_choice == '4':
#                     choice = input("Would you like to check your messages? y/n ")
#                     if choices == 'y' and loggedoff == False:
#                         #print("Blah")
#                         loginaccount.receive_message()
#                         break
#                     elif choices == 'n' and loggedoff == False:
#                         break
#                         #print("Bleh")
#                     elif loggedoff == True:
#                         print("You are not logged into an account. Please log in and try again!")
#                         break
#                 elif inner_menu_choice == '5':
#                     loginaccount.remove_friend()
#                     break
#                 elif inner_menu_choice == '6': 
#                     choicer = input("Would you like to block a user? y/n ")
#                     if choicer == 'y' and loggedoff == False:
#                         loginaccount.block_user()
#                         break
#                     elif choicer == 'n' and loggedoff == False:
#                         break
#                     elif loggedoff == True:
#                         print("You are not logged into an account. Please log in and try again!")
#                         break
#                 elif inner_menu_choice == '7':
#                     if loggedoff == False:
#                         loginaccount.send_message(loginaccount)
#                         break
#                     elif loggedoff == True:
#                         print("You are not logged into an account. Please log in and try again!")
#                         break
#                 elif inner_menu_choice == '8':
#                     if loggedoff == False:
#                         loginaccount.save_social_media()
#                         break
#                 elif inner_menu_choice == '9':
#                     if loggedoff == False:
#                         loginaccount.load_account()
#                         break
#                 elif inner_menu_choice == "10":
#                     break
#                 else:
#                     inner_menu_choice = social_network_ui.manageAccountMenu()
#         elif choice == '4':
#             print("Account logged out. Please log in again, log into another account, or create a new account.")
#             loggedoff = True
#         elif choice == "5":
#             print("Thank you for visiting. We hope that you visit again soon.")
#             break
#         else:
#             print("Your input is invalid. Try Again!")
        
#         #restart menu
#         choice = social_network_ui.mainMenu()
