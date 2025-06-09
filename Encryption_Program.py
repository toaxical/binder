
import random
import string

# identifying characters to be used for encryption and decryption

enc_chars = " " + string.punctuation + string.ascii_letters + string.digits
enc_chars = list(enc_chars)
key = enc_chars.copy()
random.shuffle(key) 


# encryption

usr_text = input("Enter text to be encrypted: \n> ")
enc_text = ""

for letter in usr_text:
    index = enc_chars.index(letter)
    enc_text += key[index]

print(f"Encrypted text is: {enc_text}")

# decryption

usr_text = input("Enter text to be decrypted: \n> ")
dec_text = ""

for character in usr_text:
    index = key.index(character)
    dec_text += enc_chars[index]

print(f"Decrypted text is: {dec_text}")