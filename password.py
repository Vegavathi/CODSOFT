import random
import string

def password (length,complexity):
    character = ''
    if 'l' in complexity:
        character += string.ascii_lowercase
    if 'u' in complexity:
        character += string.ascii_uppercase
    if 'd' in complexity:
        character += string.digits
    if 'p' in complexity:
        character += string.punctuation
    
    if not character:
        print("Error! choose complexity..")
        return None
    
    generate_password= ''.join(random.choice(character) for _ in range (length))
    return generate_password

if__name__ = "__main__"
length= int(input("Enter the length of the password:"))
print("Enter 'l' for lower case letter \n Enter 'u' for upper case letter \n Enter 'd' for digits \n Enter 'p' for puntuation")
complexity = input("Enter the complexity:")

generated_password = password(length,complexity)
print("Generated Password:" ,generated_password)
    
