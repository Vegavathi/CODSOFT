import random
import string

def password (length,complexity):
    character = ''
    if '1' in complexity:
        character += string.ascii_lowercase
    if '2' in complexity:
        character += string.ascii_uppercase
    if '3' in complexity:
        character += string.digits
    if '4' in complexity:
        character += string.punctuation
    
    if not character:
        print("Error! choose complexity..")
        return None
    
    generate_password= ''.join(random.choice(character) for _ in range (length))
    return generate_password

if__name__ = "__main__"
length= int(input("Enter the length of the password:"))
print("Enter '1' for lower case letter \n Enter '2' for upper case letter \n Enter '3' for digits \n Enter '4' for puntuation")
complexity = input("Enter the complexity:")

generated_password = password(length,complexity)
print("Generated Password:" ,generated_password)
    
