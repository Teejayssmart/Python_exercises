import logo

print(logo.logo)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def encrypt(message, shift_number):
    new_message = ''
    for char in message:
        if char in alphabet:
            char_index = alphabet.index(char)
            new_position = char_index + shift_number
            if new_position > 25:
                new_position = new_position - 26
            new_message += alphabet[new_position]
    return new_message

def decrypt(message, shift_number):
    decrypt_message = ''
    for char in message:
        if char in alphabet:
            char_index = alphabet.index(char)
            old_position = char_index - shift_number
            if old_position < 0:
                old_position = old_position + 26
            decrypt_message += alphabet[old_position]
    return decrypt_message


while True:
    usr_choice = input("Type 'E' to encrypt and 'D' to decrypt the message")
    message = input("Enter your message:\n").upper()
    shift_number = int(input("Enter the shift number:\n"))
    if usr_choice == 'E':
        encrypt_message = encrypt(message, shift_number)
        print(encrypt_message)
    elif usr_choice == 'D':
        decrypt_message = decrypt(message, shift_number)
        print(decrypt_message)
    usr_cont = input("Type 'Y' to continue or 'N to exit'")
    if usr_cont.upper() == 'N':
        break

#



