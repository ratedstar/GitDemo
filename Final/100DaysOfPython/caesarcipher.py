
from caesarcipherlogo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
def caeser(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"the {cipher_direction}d cipher text is {end_text}")

should_continue = False
while not should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)


restart = input("If you want to restart 'Yes'or'No'")
if restart == 'No':
    should_continue = True
    print("Good Bye")

# def encript(plain_text,shift_amount):
#     cipher_text = ''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position+shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The cipher text is {cipher_text}")
# def decrypted(cipher_text,shift_amount):
#     cipher_text = ''
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position-shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The plain text is {cipher_text}")
#
# if direction =='encode':
#     encript(plain_text='text', shift_amount=shift)
# elif direction=='decode':

