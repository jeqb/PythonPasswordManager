from Security import Encryptor, PasswordTools
from Common import DECRYPTED_DATABASE_NAME, ENCRYPTED_DATABASE_NAME

class EncryptionHandler():
    """
    4 layers:

    Api
    EncryptionHandler
    Stores
    Database

    This abstracts away the job of encrypting/decrypting data
    for the API. Api just passes it the data, the encryption handler
    takes care of the rest.

    Database is always encrypted. Except when an operation occurs.
    Then it gets decrypted, manipulated, then encrypted again.

    Not super efficient in terms of speed, but it works for now.
    Might implement a "cache" later to store change, and then "commit"
    all of them at the end.
    """
    def __init__(self, **kwargs):
        """
        salt_string is the encoded string form from the json file
        password_string is whatever the user passes in string form
        """
        self.database_path = kwargs['database_path']
        self.database_folder = self.database_path.replace(ENCRYPTED_DATABASE_NAME, '')

        # convert salt_string to bytes
        salt = PasswordTools.string_to_salt_bytes(kwargs['salt_string'])

        # encode password for encryption/decryption
        key = PasswordTools.password_to_bytes(password=kwargs['password_string'], salt=salt)
        self.key = key


    def encrypt_database(self):
        decrypted_file_path = self.database_folder + DECRYPTED_DATABASE_NAME
        encrypted_output = self.database_folder + ENCRYPTED_DATABASE_NAME

        # do the deed
        Encryptor.file_encrypt(self.key, decrypted_file_path, encrypted_output)

        # TODO: need to delete unencrypted file


    def decrypt_database(self):
        decrypted_file_path = self.database_folder + DECRYPTED_DATABASE_NAME
        encrypted_file = self.database_folder + ENCRYPTED_DATABASE_NAME

        Encryptor.file_decrypt(self.key, encrypted_file, decrypted_file_path)

        # TODO: need to delete encrypted file


    def get_notes(self):
        pass


    def add_note(self, content_string):
        pass


    def update_note(self, **kwargs):
        pass


    def delete_note(self, **kwargs):
        pass


    def search_note_by_content(self, search_string):
        pass


    def get_passwords(self):
        pass


    def add_password(self, **kwargs):
        pass


    def update_password(self, **kwargs):
        pass


    def delete_password(self, **kwargs):
        pass