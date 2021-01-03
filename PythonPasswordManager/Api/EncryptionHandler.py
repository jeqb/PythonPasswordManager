import os
import cryptography
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
        
        self.database_folder = kwargs['database_folder_path']
        
        self.connection_string = 'sqlite:///' + self.database_folder + '/' + DECRYPTED_DATABASE_NAME
        self.engine = create_engine(self.connection_string)
        self.note_store = NoteStore(self.engine)
        self.entry_store = EntryStore(self.engine)

        self.password_string = kwargs['password_string']


    def encrypt_database(self):
        decrypted_input = self.database_folder + '/' + DECRYPTED_DATABASE_NAME
        encrypted_output = self.database_folder + '/' + ENCRYPTED_DATABASE_NAME

        salt = PasswordTools.make_salt()
        key = PasswordTools.password_to_bytes(password=self.password_string,
            salt=salt)

        Encryptor.encrypt_file(key=key, input_file=decrypted_input,
            output_file=encrypted_output)

        self.attach_salt(salt)

        # delete unencrypted file
        os.remove(decrypted_input)


    def decrypt_database(self):
        decrypted_output = self.database_folder + '/' + DECRYPTED_DATABASE_NAME
        encrypted_input = self.database_folder + '/' + ENCRYPTED_DATABASE_NAME

        salt = self.detach_salt()
        key = PasswordTools.password_to_bytes(password=self.password_string,
            salt=salt)

        try:
            Encryptor.decrypt_file(key=key, input_file=encrypted_input,
                output_file=decrypted_output)
        except cryptography.fernet.InvalidToken as e:
            self.attach_salt(salt)
            raise e
        else:
            # delete encrypted file
            os.remove(encrypted_input)


    def attach_salt(self, salt: bytes):
        """
        The database file should currently be encrypted, but no salt is attached
        to it yet. Grab the salt from self.salt, and append it to the front of the
        encrypted database file.
        """
        
        # first verify there is an encrypted file
        encrypted_file = self.database_folder + '/' + ENCRYPTED_DATABASE_NAME
        if not os.path.exists(encrypted_file):
            raise Exception("No encrypted file was found")
        
        # get the raw encrypted file
        with open(encrypted_file, 'rb') as file:
            raw_encrypted_rile = file.read()
        
        # do the deed
        salty_file = salt + raw_encrypted_rile

        # overwrite sodium free file with salty file
        with open (encrypted_file, 'wb') as file:
            file.write(salty_file)


    def detach_salt(self) -> bytes:
        """
        Salt is currently appended to the front of the encrypted database file
        as bytes. Specifically the first 16 bytes on the file are the salt.
        Remove those bytes from the file, and store them as self.salt
        """

        # first verify there is an encrypted file
        encrypted_file = self.database_folder + '/' + ENCRYPTED_DATABASE_NAME
        if not os.path.exists(encrypted_file):
            raise Exception("No encrypted file was found")
        
        # then open the salty file
        with open(encrypted_file, 'rb') as file:
            raw_salty_file = file.read()

        # salt
        salt = raw_salty_file[:16]

        # remove the salt
        sodium_free_encrypted_file = raw_salty_file[16:]

        # overwrite salty file with sodium free file
        with open (encrypted_file, 'wb') as file:
            file.write(sodium_free_encrypted_file)

        return salt


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


    def search_password_by_website(self, website_string):
        self.decrypt_database()
        results = self.entry_store.search_entry_by_website(website_string)
        self.encrypt_database()

        return results


    def search_password_by_website_and_category(self, website_string, category_string):
        self.decrypt_database()
        results = self.entry_store.search_entry_by_website_and_category(
            website_string, category_string
            )
        self.encrypt_database()

        return results