from cryptography.fernet import Fernet


class Encryptor():

    @staticmethod
    def file_encrypt(key: bytes, original_file: str, encrypted_file: str) -> None:
        """
        Give a 64bit encoded 32-byte key. Give it the file path to
        original_file and then the file path to the desired output.
        """
        
        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open (encrypted_file, 'wb') as file:
            file.write(encrypted)

    @staticmethod
    def file_decrypt(key: bytes, encrypted_file: str, decrypted_file: str) -> None:
        """
        Give a 64bit encoded 32-byte key. Give it the path to the enrypted file
        and then give it the path where you want to output the decrypted file
        """

        f = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)