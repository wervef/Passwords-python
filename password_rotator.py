def password_rotator():
    password = input("Enter a password to rotate ")
    rotated_password = ""
    password_copy = password
    while len(rotated_password) != len(password):
        rotated_password = rotated_password + password_copy[-1]
        password_copy = password_copy[:-1]
    #print(rotated_password)
    with open('rotated_password.txt', 'w') as file:
        file.write(password + ", " + rotated_password)    

password_rotator()