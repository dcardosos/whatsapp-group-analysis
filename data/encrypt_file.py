from cryptography.fernet import Fernet

key = input('Enter your password: ')
cipher = Fernet(key)

filename = 'chat_tagarelas.txt'


with open(filename, 'rb') as f:
    e_file = f.read()

encrypted_file = cipher.encrypt(e_file)

with open('encrypted_'+ filename, 'wb') as ef:
    ef.write(encrypted_file)

