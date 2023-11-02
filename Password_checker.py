import random
import string
from cryptography.fernet import Fernet


def passwords_checker():
    """Checks whether or not each password in a list of passwords is secure, and improves them if they're not"""
    new_passwords = []
    with open('Passwords.txt', 'r') as file:
        text = file.read()
        password_list = text.split()
        #Reads the passwords file and makes a list including every password in it
    for single_password in password_list:
        if password_checker(single_password) == "Password fails" or password_checker(single_password) == "Password is too short":
            #If the password isn't secure enough it will be improved and added to the new list of passwords
            while len(single_password) < 12:
                extra_characters = str(random.randint(1, 9)) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.punctuation)
                single_password = single_password + extra_characters
            new_passwords = new_passwords + [single_password]
        else:
            #If the password is already secure enough then it will be added to the new list of passwords without any change
            new_passwords = new_passwords + [single_password]
    print(new_passwords)
    #The new list of passwords will be shown


def password_checker(pswrd):
    password_copy = pswrd
    lower_case = False
    upper_case = False
    numbers = False
    other = False
    #All password character requirement are set to False by default
    if len(pswrd) < 12:
        return("Password is too short")
    #If the password is shorter than 12 character then it will fail
    else:
        while password_copy != "":
            char = password_copy[0]
            if char.islower() == True:
                lower_case = True
            if char.isupper() == True:
                upper_case = True
            if char.isdigit() == True:
                numbers = True
            if char.islower() == False and char.isupper() == False and char.isdigit() == False:
                other = True
            password_copy = password_copy[1:]
            #Each character in the password gets checked. To be considered secure the password needs to contain at least one lower case letter, one upper case letter, one digit and one other character that is none of those
        if lower_case == True and upper_case == True and other == True:
            return("Password passes")
        #If the password contains all character requirements than it passes
        else:
            return("Password fails")
        #If the password doesn't meet all the character requirement than it fails

passwords_checker()