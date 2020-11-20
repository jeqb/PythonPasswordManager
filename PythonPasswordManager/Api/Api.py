from sqlalchemy import create_engine

from Storage import NoteStore, Note

class Api():
    """
    The Ui will use this for behavior and actions.
    """
    def __init__(self, database_path):
        self.database_path = database_path
        self.engine = create_engine(database_path)
        self.note_store = NoteStore(self.engine)


    def get_notes(self):
        result = self.note_store.get_notes()

        return result