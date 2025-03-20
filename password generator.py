import random
import string

def generate_password(length=12):

    characters = string.ascii_letters + string.digits + string.punctuation


    password = ''.join(random.choice(characters) for i in range(length))

    return password


try:
    length = int(input("Enter the desired length of the password: "))
    if length < 6:
        print("Password length should be at least 6 characters for security.")
    else:
    
        print(f"Generated Password: {generate_password(length)}")
except ValueError:
    print("Please enter a valid number!")
