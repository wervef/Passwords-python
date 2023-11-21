import random
import string
from cryptography.fernet import Fernet

def password_generator(number_of_characters):
    random_characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    while len(password) != int(number_of_characters):
        password = password + random.choice(random_characters)
    return password

def password_list_generator():
    password_list = []
    while len(password_list) != 50:
        password_list = password_list + [password_generator(12)]
    return password_list

def encrypt_passwords():
    data_to_encrypt = password_list_generator()
    key = Fernet.generate_key()

    # Initialize a Fernet cipher with the key
    cipher = Fernet(key)

    # Encrypt a list of strings
    encrypted_data = []
    for item in data_to_encrypt:
        encrypted_item = cipher.encrypt(item.encode())
        encrypted_data.append(encrypted_item)

    # Decrypt the data
    decrypted_data = []
    for item in encrypted_data:
        decrypted_item = cipher.decrypt(item).decode()
        decrypted_data.append(decrypted_item)

    #print("Original Data:", data_to_encrypt)
    #print("Encrypted Data:", encrypted_data)
    #print("Decrypted Data:", decrypted_data)
    #print("Encryption Key:", key)

    with open('list_of_50_encrypted_passwords.txt', 'w') as file:
        # Iterates through the list and writes each element to a file named list_of_50_encrypted_passwords.txt
        for item in encrypted_data:
            file.write(str(item) + '\n') 

def password_to_txt():
    list_of_passwords = password_list_generator()
    with open('list_of_50_passwords.txt', 'w') as file:
        # Iterates through the list and writes each element to a file named list_of_50_passwords.txt
        for item in list_of_passwords:
            file.write(str(item) + '\n')    



encrypt_passwords()
password_to_txt()
