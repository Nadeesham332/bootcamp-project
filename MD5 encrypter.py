# md5 encrypting programme by W.P. NADEESHA MADURANGA (nadeesham332@gmail.com)
import hashlib


# prints the encryption of plain text
def md5_encryption(clr_text):
    encrypted = hashlib.md5(clr_text.encode())
    print(f'MD5 Hash: {encrypted.hexdigest()}')


# Take the user input
text = input("Your String: ")
md5_encryption(text)
