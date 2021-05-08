from cryptography.fernet import Fernet

def decrypt(key):

   # key = input('Enter your key: ')

    cipher = Fernet(key)

    with open('data/encrypted_chat_tagarelas.txt', 'rb') as f:
        encrypted_data = f.read()

    decrypted_file = cipher.decrypt(encrypted_data)

    #print(decrypted_file.decode())

    with open('data/chat_tagarelas.txt', 'wb') as df:
        df.write(decrypted_file)
    
    return 'successfully decrypted'
