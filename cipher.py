alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(text, shift):
    cipher_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift)%26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"encrypted text is : {cipher_text}")

def decryption(text, shift):
    cipher_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift)%26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"encrypted text is : {cipher_text}")

while True:
    command = input('enter encrypt for encryption or decrypt for decryption:\n')
    text = input('enter text:\n')
    shift = int(input('enter the shift key\n'))
    if command == "encrypt":
        encryption(text=text, shift=shift)
    if command =="decrypt":
        decryption(text=text, shift=shift)
    do = input('Do you want to continue, enter yes to continue or no to exit:\n')
    if do == 'no':
        print('goodbye.......\n')
        break
    elif do == 'yes':
        continue




