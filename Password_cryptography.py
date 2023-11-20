from cryptography.fernet import Fernet

def encrypt_passwords():
    data_to_encrypt = ["Password1234wD-", "Passwords123!", "1!@2Password3#4%678"]
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

    for item in encrypted_data:
        print (item)
    for item in decrypted_data:
        print (item)        

    

encrypt_passwords() 