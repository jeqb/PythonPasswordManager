import cryptography
from sqlalchemy import create_engine

from Common.Exceptions import InvalidPasswordException
from Storage import NoteStore, Note, EntryStore, Entry

from .EncryptionHandler import EncryptionHandler

class Api():
    """
    The Ui will use this for behavior and actions.
    """
    def __init__(self, **kwargs):
        self.database_path = kwargs['database_folder_path']
        self.connection_string = 'sqlite:///' + self.database_path
        self.engine = create_engine(self.connection_string)
        self.note_store = NoteStore(self.engine)
        self.entry_store = EntryStore(self.engine)

        # EncryptionHandler
        self.handler = EncryptionHandler(**kwargs)


    def test_database_connection(self):
        """
        Check to see if system can connect to database given a database path
        """
        try:
            self.handler.decrypt_database()
        except cryptography.fernet.InvalidToken:
            raise InvalidPasswordException("Could not decrypt database with this password.")
        else:
            self.handler.encrypt_database()


    def decrypt_database(self):
        self.handler.decrypt_database()


    def encrypt_database(self):
        self.handler.encrypt_database()


    def get_notes(self):
        result = self.handler.get_notes()

        return result


    def add_note(self, content_string):
        note = Note(Content=content_string)

        self.handler.add_note(note)


    def update_note(self, **kwargs):
        note = Note(
            Id = kwargs['Id'],
            Content = kwargs['Content']
        )

        self.handler.update_note(note)


    def delete_note(self, **kwargs):
        note = Note(
            Id = kwargs['Id'],
            Content = kwargs['Content']
        )

        self.handler.delete_note(note)


    def search_note_by_content(self, search_string):
        results = self.handler.search_note_by_content(search_string)

        return results


    def get_passwords(self):
        results = self.handler.get_passwords()

        return results


    def add_password(self, **kwargs):
        entry = Entry(
            Website = kwargs['Website'],
            Username = kwargs['Username'],
            Email = kwargs['Email'],
            Password = kwargs['Password'],
            Category = kwargs['Category'],
            Note = kwargs['Note']
        )

        self.handler.add_password(entry)


    def update_password(self, **kwargs):
        entry = Entry(
            Id = kwargs['Id'],
            Website = kwargs['Website'],
            Username = kwargs['Username'],
            Email = kwargs['Email'],
            Password = kwargs['Password'],
            Category = kwargs['Category'],
            Note = kwargs['Note']
        )

        self.handler.update_password(entry)


    def delete_password(self, **kwargs):
        entry = Entry(
            Id = kwargs['Id'],
            Website = kwargs['Website'],
            Username = kwargs['Username'],
            Email = kwargs['Email'],
            Password = kwargs['Password'],
            Category = kwargs['Category'],
            Note = kwargs['Note']
        )

        self.handler.delete_password(entry)