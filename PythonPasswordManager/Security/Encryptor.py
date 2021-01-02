from cryptography.fernet import Fernet


class Encryptor():

    @staticmethod
    def encrypt_file(key: bytes, input_file: str, output_file: str) -> None:
        """
        Give a 64bit encoded 32-byte key. Give it the file path to
        input_file and then the file path to the desired output.
        """
        
        f = Fernet(key)

        with open(input_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open (output_file, 'wb') as file:
            file.write(encrypted)

    @staticmethod
    def decrypt_file(key: bytes, input_file: str, output_file: str) -> None:
        """
        Give a 64bit encoded 32-byte key. Give it the path to the enrypted file
        and then give it the path where you want to output the decrypted file
        """

        f = Fernet(key)

        with open(input_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(output_file, 'wb') as file:
            file.write(decrypted)