import os
from sqlalchemy import create_engine

from Storage import NoteStore, Note, EntryStore, Entry
from Security import Encryptor, PasswordTools
from Common.Constants import DECRYPTED_DATABASE_NAME, ENCRYPTED_DATABASE_NAME

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
        kwargs:
            database_path: str
            salt_string: str
            password_string: str


        salt_string is the encoded string form from the json file
        password_string is whatever the user passes in string form
        """

        self.database_path = kwargs['database_path']
        self.database_folder = self.database_path.replace(DECRYPTED_DATABASE_NAME, '')
        
        self.connection_string = 'sqlite:///' + self.database_path
        self.engine = create_engine(self.connection_string)
        self.note_store = NoteStore(self.engine)
        self.entry_store = EntryStore(self.engine)

        # convert salt_string to bytes
        salt = PasswordTools.string_to_salt_bytes(kwargs['salt_string'])

        # encode password for encryption/decryption
        key = PasswordTools.password_to_bytes(password=kwargs['password_string'], salt=salt)
        self.key = key


    def encrypt_database(self):
        decrypted_file_path = self.database_folder + DECRYPTED_DATABASE_NAME
        encrypted_output = self.database_folder + ENCRYPTED_DATABASE_NAME

        Encryptor.file_encrypt(self.key, decrypted_file_path, encrypted_output)

        # delete unencrypted file
        os.remove(decrypted_file_path)


    def decrypt_database(self):
        decrypted_file_path = self.database_folder + DECRYPTED_DATABASE_NAME
        encrypted_file_path = self.database_folder + ENCRYPTED_DATABASE_NAME

        Encryptor.file_decrypt(self.key, encrypted_file_path, decrypted_file_path)

        # delete encrypted file
        os.remove(encrypted_file_path)


    def get_notes(self):
        self.decrypt_database()

        result = self.note_store.get_notes()

        self.encrypt_database()

        return result


    def add_note(self, note):
        self.decrypt_database()
        self.note_store.create_note(note)
        self.encrypt_database()


    def update_note(self, note):
        self.decrypt_database()
        self.note_store.update_note(note)
        self.encrypt_database()


    def delete_note(self, note):
        self.decrypt_database()
        self.note_store.delete_note(note)
        self.encrypt_database()


    def search_note_by_content(self, search_string):
        self.decrypt_database()
        results = self.note_store.search_note_by_content(search_string)
        self.encrypt_database()

        return results


    def get_passwords(self):
        self.decrypt_database()
        results = self.entry_store.get_entries()
        self.encrypt_database()

        return results


    def add_password(self, entry):
        self.decrypt_database()
        self.entry_store.create_entry(entry)
        self.encrypt_database()


    def update_password(self, entry):
        self.decrypt_database()
        self.entry_store.update_entry(entry)
        self.encrypt_database()


    def delete_password(self, entry):
        self.decrypt_database()
        self.entry_store.delete_entry(entry)
        self.encrypt_database()