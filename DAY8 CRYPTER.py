# import random
# def function(name,location):
#     print(f"How are u {name}")
#     print(f"How are weather is {location}")
#
#
# function(location="san francisco", name="mevlut")
# sayilistesi=[2,3,5,7,9]
#
# def prime_checker(number):
#     for check in range(2,number):
#         if number%check==0:
#             is_prime=False
#
#     if is_prime==True:
#         print("Number is a prime.")
#     else:
#         print("Number isn't prime")

# prime_checker(number=49)
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a', 'b' ,'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b' ,'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# 26 25
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
           position=alphabet.index(letter)
           new_position=position+shift_amount
           new_letter=alphabet[new_position]
           cipher_text+=new_letter
        else:
           new_letter+=letter
           cipher_text += new_letter
    print(f"the encoded text is {cipher_text}")

def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position-shift_amount
            new_letter = alphabet[new_position]
            cipher_text+=new_letter
        else:
            new_letter+= letter
            cipher_text+=new_letter
    print(f"the encoded text is {cipher_text}")

if direction=="encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction=="decode":
    decrypt(plain_text=text, shift_amount=shift)








