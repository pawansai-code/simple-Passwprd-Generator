import string
# I’m importing the string module to access character sets like lowercase, punctuation, etc.
import secrets
# I’m importing secrets to securely generate random characters for the password

def contains_upper(password: str) -> bool:
    # I’m defining a function to check if the password contains any uppercase letter
    for char in password:
    # I’m looping through each character in the password
        if char.isupper():
        # I’m checking if the current character is an uppercase letter
            return True
            # I return True because an uppercase letter was found

    return False
    # I return False because no uppercase letter was found

def contains_symbols(password: str) -> bool:
# I’m defining a function to check if the password contains any symbol
    for char in password:
    # I’m looping through each character in the password
        if char in string.punctuation:
        # I’m checking if the character is a punctuation symbol
            return True
            # I return True because a symbol was found

    return False
    # I return False because no symbols were found

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
# I’m defining a function to generate a random password
    combination: str = string.ascii_lowercase + string.digits
    # I’m initializing the combination with lowercase letters and digits

    if symbols:
    # I’m checking if symbols should be included in the password
        combination += string.punctuation
        # I’m adding symbols to the combination set

    if uppercase:
    # I’m checking if uppercase letters should be included
        combination += string.ascii_uppercase
        # I’m adding uppercase letters to the combination set

    combination_length = len(combination)
    # I’m storing the length of the final character set
    new_password: str = ''
    # I’m initializing an empty string for the new password

    for _ in range(length):
    # I’m repeating the loop for the number of characters requested
        new_password += combination[secrets.randbelow(combination_length)]
        # I’m selecting a random character and appending it to the password

    return new_password
    # I return the generated password

if __name__ == '__main__':
# I’m ensuring this block runs only when this script is executed directly
    for i in range(1, 6):
    # I’m generating and printing 5 passwords, numbered 1 to 5
        new_pass: str = generate_password(length=10, symbols=False, uppercase=False)
        # I’m generating a password with given conditions
        specs: str = f'U: {contains_upper(new_pass)}, s: {contains_symbols(new_pass)}'
        # I’m checking for uppercase and symbols in the password
        print(f'{i} -> {new_pass} ({specs})')
        # I’m printing the password along with its specs
