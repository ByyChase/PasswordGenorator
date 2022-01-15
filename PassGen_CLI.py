import random
import os

#Declare Global Variables
debug = False
password = ""

def main():

    #Declare Variables
    upper_case = ['1) [X] Upper Case: ABCDEFGHIJKLMNOPQRSTUVWXYZ', '1) [] Upper Case: ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    lower_case = ['2) [X] Lower Case: abcdefghijklmnopqrstuvwxyz', '2) [] Lower Case: abcdefghijklmnopqrstuvwxyz']
    numbers = ['3) [X] Numbers: 1234567890', '3) [] Numbers: 1234567890']
    special_characters = ['4) [X] Special Characters: !@#$%^&*()<>?', '4) [] Special Characters: !@#$%^&*()<>?']
    all_characters = [upper_case, lower_case, numbers, special_characters]
    characters_included = [1, 0, 0, 0]
    accepted_numbers = ['1', '2', '3', '4']
    accepted_letters = ['a', 'd']
    user_input = ""
    password = ""
    error_1 = False
    error_2 = False

    os.system('cls' if os.name == 'nt' else 'clear')


    




    while user_input.lower() != 'exit':

        print("\n\n ------------------------------------------")
        print('|' + '\033[1m' +  'Welcome to the Python Password Genorator' + '\033[0m' + ' |')
        print(" ------------------------------------------\n\n")


        print("Character Groups Incuded:\n\n")
        count = 0
        for x in all_characters:
            print(x[characters_included[count]])
            count+=1

        print("\n- Type 'D *number you would like to deselect*' to remove those characters from the password generation")
        print("- Type 'A *number you would like to select*' to add those characters to the password generation")
        print("- Enter the length you want your password to be and press enter to generator a password")
        print("- Type 'Exit' at anytime to quit")
        print("\n\nYour Password: " + password)

        if error_1 == True:
            print('\n' + '\033[31m' + 'ERROR: That character type is already removed' + '\033[39m')
            error_1 = False

        elif error_2 == True:
            print('\n' + '\033[31m' + 'ERROR: That character type is already removed' + '\033[39m')
            error_2 = False

        else:
            print("\n")

        user_input = input("\nPlease Make an Input...\n\nInput:")

        if user_input[0:1].lower() == 'a':

            if user_input[2:3] in accepted_numbers:

                    if characters_included[(int(user_input[2:3]) - 1)] == 0:

                        error_1 = True

                    else:

                        characters_included[(int(user_input[2:3]) - 1)] = 0

        elif user_input[0:1].lower() == 'd':

            if user_input[2:3] in accepted_numbers:

                    if characters_included[(int(user_input[2:3]) - 1)] == 1:

                        error_2 = True

                    else:

                        characters_included[(int(user_input[2:3]) - 1)] = 1

        elif user_input.isnumeric():
            
            
            password = generate_password(user_input, characters_included)



        if user_input.lower() == 'exit':

            print("\n\nHave a Nice Day!")    

        else:

            os.system('cls' if os.name == 'nt' else 'clear')
            
            



def generate_password(password_length, included_characters):

    #Declare Variables
    lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']         #List of all possible lowercase letters
    upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']         #List of all possible uppercase letters
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']                                                                                                #List of all possible numbers
    symbols_list = {'`','~','!','@','#','$','%','^','&','*','(',')','_','-','{','[','}','}','|',':','<','>','?'}                                                    #List of all possible symboles
    list_of_all = [upper_case_letters, lower_case_letters, number_list, symbols_list]                                                                               #List fo all the possible character lists
    final_used_list = []                                                                                                                                            #List of all the lists the user chose to use for their password
    count = 0                                                                                                                                                       #Used to add lists to the final list and to generate random numbers
    password = ""                                                                                                                                             #The password returned to the user                                                                                                                                         

    
    for x in included_characters:

        if debug:
            print("DEBUG: Checking Characters: " + str(x))
        
        if x == 0:
            final_used_list.append(list_of_all[count])

        count+=1

    for x in range(int(password_length)):

        random_list = list(random.choice(final_used_list)
        )
        if debug:

            print(random_list)


        random_character = random.choice(random_list)

        if debug:

            print(random_character)

        password += str(random_character)

        
    return password
        
        

    


if __name__ == '__main__':
    main()
            
        



