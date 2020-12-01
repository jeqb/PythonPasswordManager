from sqlalchemy import create_engine

from Storage import NoteStore, Note, EntryStore, Entry

class Api():
    """
    The Ui will use this for behavior and actions.
    """
    def __init__(self, database_path):
        self.database_path = database_path
        self.connection_string = 'sqlite:///' + self.database_path
        self.engine = create_engine(self.connection_string)
        self.note_store = NoteStore(self.engine)
        self.entry_store = EntryStore(self.engine)


    def test_database_connection(self):
        """
        Check to see if system can connect to database given a database path
        """
        try:
            connection = self.engine.connect()
        except Exception as e:
            raise e
        finally:
            connection.close()


    def get_notes(self):
        result = self.note_store.get_notes()

        return result


    def add_note(self, content_string):
        note = Note(Content=content_string)

        self.note_store.create_note(note)


    def update_note(self, **kwargs):
        note = Note(
            Id = kwargs['Id'],
            Content = kwargs['Content']
        )

        self.note_store.update_note(note)


    def delete_note(self, **kwargs):
        note = Note(
            Id = kwargs['Id'],
            Content = kwargs['Content']
        )

        self.note_store.delete_note(note)


    def search_note_by_content(self, search_string):
        results = self.note_store.search_note_by_content(search_string)

        return results


    def get_passwords(self):
        results = self.entry_store.get_entries()

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

        self.entry_store.create_entry(entry)


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

        self.entry_store.update_entry(entry)


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

        self.entry_store.delete_entry(entry)