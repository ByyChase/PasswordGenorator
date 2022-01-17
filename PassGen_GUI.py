import PySimpleGUI as gui
import random



def main(): 
    layout = [

        [gui.Text("Python Password Generator")],
        [gui.InputText(values=("Password") key="Password_Box")],
        [gui.Button("Generate")]
        


    ]



    windows = gui.Window(title = "Password Genorator", layout = layout)

    while True:
        event, values = windows.read()

        if event == "Generate":
            password = generate_password(15, [0,0,0,0])
            windows.Element("Password_Box").Update(values=[password])

        if event == gui.WIN_CLOSED:
            break


    windows.close()


def generate_password(password_length, included_characters = None):

    print("hello")
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