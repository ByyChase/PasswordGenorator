import random
import os

#Declare Global Variables
debug = False
password = ""

def main():

    #Declare Variables
    upper_case = ['1) [X] Upper Case: ABCDEFGHIJKLMNOPQRSTUVWXYZ', '1) [] Upper Case: ABCDEFGHIJKLMNOPQRSTUVWXYZ']                                                  #A list of the two possible outputs for the CLI for the upper_case character set                                                 
    lower_case = ['2) [X] Lower Case: abcdefghijklmnopqrstuvwxyz', '2) [] Lower Case: abcdefghijklmnopqrstuvwxyz']                                                  #A list of the two possible outputs for the CLI for the lower_case character set 
    numbers = ['3) [X] Numbers: 1234567890', '3) [] Numbers: 1234567890']                                                                                           #A list of the two possible outputs for the CLI for the number character set 
    special_characters = ['4) [X] Special Characters: !@#$%^&*()<>?', '4) [] Special Characters: !@#$%^&*()<>?']                                                    #A list of the two possible outputs for the CLI for the special character set 
    all_characters = [upper_case, lower_case, numbers, special_characters]                                                                                          #A list of the list of possible character set outputs.
    characters_included = [0, 0, 0, 0]                                                                                                                              #List of numbers corosponding to the all_characters list. Used to store if a character set is included or not                                   
    accepted_numbers = ['1', '2', '3', '4']                                                                                                                         #Numbers accepted by the user input to add or remove character sets
    user_input = ""                                                      
    password = ""
    error_1 = False                                                                                                                                                 #Boolean used to determine if the error message about the character set already being added should be shown
    error_2 = False                                                                                                                                                 #Boolean used to determine if the error message about the character set already being removed should be shown
    options_show = True                                                                                                                                             #Boolean used to determine if the options for the program should be shown

    #Clearing the OS CLI to make it look the same througout use
    os.system('cls' if os.name == 'nt' else 'clear')

    #While loop that runs the program until the user wants to stop
    while user_input.lower() != 'exit':

        #Printing the welcome message in bold
        print("\n\n ------------------------------------------")
        print('|' + '\033[1m' +  'Welcome to the Python Password Genorator' + '\033[0m' + ' |')
        print(" ------------------------------------------\n\n")

        #printing out the groups of characters and if they are included or not
        #This is based on the characters_included list. The list corosponds to the all_characters list.
        #If the numbers corosponding to the group of characters is set to 0 it will be included and printed with an X in the selection box
        #If the number is 1 it will not be inlcuded and will not be printed with an x in the selection box
        print("Character Groups Incuded:\n\n")
        count = 0
        for x in all_characters:
            print(x[characters_included[count]])
            count+=1


        #printing out the options the user has in the program. The user can disable this by typing 'options' in the input. options_show is set to false in that instance
        if options_show == True:

            print("\n- Type 'options' at any time to show or hide these options")
            print("- Type 'D *number you would like to deselect*' to remove those characters from the password generation")
            print("- Type 'A *number you would like to select*' to add those characters to the password generation")
            print("- Enter the length you want your password to be and press enter to generator a password")
            print("- Type 'Exit' at anytime to quit")

        #Printing the users genorated password
        print("\n\nYour Password: " + password)

        #printing an error to the user if they chose to remove a character set if it was already added
        if error_1 == True:
            print('\n' + '\033[31m' + 'ERROR: That character type is already added' + '\033[39m')
            error_1 = False

        #printing an error to the user if they chose a character set that was already removed
        elif error_2 == True:
            print('\n' + '\033[31m' + 'ERROR: That character type is already removed' + '\033[39m')
            error_2 = False

        #If there are no errors printing a blank line to keep the CLI looking the same 
        else:
            print("\n")

        #Taking the users input
        user_input = input("\nPlease Make an Input...\n\nInput:")

        #Checking to see if the user wants to add a character set
        if user_input[0:1].lower() == 'a':
            
            #Checking to make sure the user entered a number we can work with
            if user_input[2:3] in accepted_numbers:
                    
                    #Checking to see if the character was already added
                    if characters_included[(int(user_input[2:3]) - 1)] == 0:
                        
                        #If the set was already added an error will be shown to the user
                        error_1 = True

                    else:
                        
                        #If the set was not added already then it is added
                        characters_included[(int(user_input[2:3]) - 1)] = 0

        #Checking to see if the user was to remove a character set
        elif user_input[0:1].lower() == 'd':

            #Making sure they entered a number we can work with
            if user_input[2:3] in accepted_numbers:

                    #Checking to see if the set has already been removed 
                    if characters_included[(int(user_input[2:3]) - 1)] == 1:

                        #If the set was already removed an error will be shown
                        error_2 = True

                    else:
                        
                        #If the character set was not already removed then it is removed
                        characters_included[(int(user_input[2:3]) - 1)] = 1

        #Checking to see if the user wants to remove the options in the CLI
        elif user_input.lower() == 'options':

            #If the options are already showing we will remove them
            if options_show == True:
                options_show = False

            #If the options are removed then we will show them
            else:
                options_show = True

        #Checking to see if the users input is just a number
        elif user_input.isnumeric():
            
            #If the input is just a number, that input is password into the generator function to make a password
            password = generate_password(user_input, characters_included)


        #Checking to see if the user wants to exit the program
        if user_input.lower() == 'exit':

            print("\n\nHave a Nice Day!")    

        else:

            #Clearing the CLI
            os.system('cls' if os.name == 'nt' else 'clear')
            

def generate_password(password_length, included_characters = None):

    #Declare Variables
    lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']         #List of all possible lowercase letters
    upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']         #List of all possible uppercase letters
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']                                                                                                #List of all possible numbers
    symbols_list = {'`','~','!','@','#','$','%','^','&','*','(',')','_','-','{','[','}','}','|',':','<','>','?'}                                                    #List of all possible symboles
    list_of_all = [upper_case_letters, lower_case_letters, number_list, symbols_list]                                                                               #List fo all the possible character lists
    final_used_list = []                                                                                                                                            #List of all the lists the user chose to use for their password
    count = 0                                                                                                                                                                                         
    is_1 = 0                                                                                                                                                        #Counter variable to make sure the user didnt uncheck all the character types                                                                                                                                          
    password = ""                                                                                                                                                   #The password genorated for the user                                                                                                                                                                                                                                                                                    

    #For loop to go through the characters sets the user wants to use in the password
    for x in included_characters:
        
        #If the user wants the character set in their program then the list is added to a list of the wanted characters
        if x == 0:

            final_used_list.append(list_of_all[count])

        #If the user doesnt want the character set added to the password then we keep track ofhow many they dont want
        else:
    
            is_1+=1

        count+=1

    #If the user doesnt want 4 of the sets then that means they dont want any. An error is returned to the user 
    if is_1 == 4:

        return '\033[31m' + 'Empty Password' + '\033[39m'

    #A for loop that runs for the length of the password they want
    for x in range(int(password_length)):

        #A random list is picked from the list the user wanted
        random_list = list(random.choice(final_used_list))
        #A random character is pick from the random list picked above
        random_character = random.choice(random_list)
        #The character us added to the password
        password += str(random_character)
    #The password is returned to the user
    return password
        
        
if __name__ == '__main__':
    main()
            
        



