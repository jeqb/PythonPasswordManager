import os
import base64
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


def password_to_bytes(password: str, salt:bytes, byte_size: int=32) -> bytes:
    """
    takes a password and a salt (in bytes) and converts to a
    base 64 encoded key.
    example usage:
        password = "my secret password"
        salt = os.urandom(16)
        key = password_to_bytes(password, salt)
        print(key)
    """
    
    password_bytes = bytes(password.encode())

    kdf = Scrypt(salt=salt, length=byte_size, n=2**14, r=8,p=1)

    key = kdf.derive(password_bytes)

    encode_key = base64.b64encode(key)

    return encode_key


def make_salt():
    return os.urandom(16)