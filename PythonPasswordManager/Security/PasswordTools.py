import os
import base64
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

from Common.Constants import SETTINGS_FILE_NAME

class PasswordTools():

    @staticmethod
    def password_to_bytes(password: str, salt:bytes, byte_size: int=32) -> bytes:
        """
        takes a password and a salt (in bytes) and converts to a
        base 64 encoded key. Convert to 32-bytes for the encryption tool.
        
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


    @staticmethod
    def make_salt() -> bytes:
        """
        Per docs, returns random bytes. this is needed for the encryption algorithm
        https://docs.python.org/3/library/os.html
        """
        return os.urandom(16)


    @staticmethod
    def salt_to_string(salt_bytes) -> str:
        """
        Need to store the salt used for encryption. The Encryptor
        works with the salt as a byte array. This converts that into a string for storage
        """
        salt_string = base64.b64encode(salt_bytes).decode('utf-8')

        return salt_string


    @staticmethod
    def string_to_salt_bytes(string) -> bytes:
        """
        This ingests a salt stored as a string, and converts it back to
        a byte array or something like that.
        """
        byte_array = base64.b64decode(string)

        return byte_array


    @staticmethod
    def verify_salty_string(salty_string) -> None:
        """
        various checks to make sure the salt_string from the json
        config file didn't get corrupted.
        """
        
        # case 1
        if len(salty_string) != 24:
            # salty_string is always 24 characters long
            raise Exception(f"Corrupted Salt in {SETTINGS_FILE_NAME}: salty_string length != 24")

        # case 2
        elif salty_string[-2:] != '==':
            # the stored salts always have a '==' at the end of them.
            # lame, but it works.
            raise Exception(f"Corrupted Salt in {SETTINGS_FILE_NAME}: salty_string doesn't have a \'==\' at the end")

        # case 3
        elif len(PasswordTools.string_to_salt_bytes(salty_string)) != 16:
            # salt is always 16 bytes long
            raise Exception(f"Corrupted Salt in {SETTINGS_FILE_NAME}: salt length != 16 bytes")