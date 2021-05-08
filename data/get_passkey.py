import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def get_passkey(pass_from_user):
    #pass_from_user = input('Please enter your password: ')
    password = pass_from_user.encode()

    mysalt = b'G\xe6Dpy#\x96\x8bC\x17\x84\x06\xa2\xa4\xc0\t' 
    kdf = PBKDF2HMAC (
            algorithm=hashes.SHA256,
            length=32,
            salt=mysalt,
            iterations=100000,
            backend=default_backend()
            )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    #print(key.decode())
    return key
