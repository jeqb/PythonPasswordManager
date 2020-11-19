from .Note import Note

from sqlalchemy.orm import Session

class NoteStore:
    """
    Provides the CRUD functionality for Notes
    """
    def __init__(self, engine):
        """
        example:
            from sqlalchemy import create_engine
            engine = create_engine('sqlite:///database.db')
            note_store = NoteStore(engine)
        """
        self.engine = engine


    def get_notes(self):
        """
        example usage:
            result = note_store.get_notes()
            for row in result:
                print(row.Id)
                print(row.Content)
        """
        session = Session(self.engine)
        result = session.query(Note).all()
        session.close()

        return result


    def get_note_by_id(self, id):
        """
        example usage:
            note = note_store.get_note_by_id(1)
            print(note.Id)
            print(note.Content)
        """
        session = Session(self.engine)
        result = session.query(Note).filter_by(Id=id).first()
        session.close()

        return result


    def create_note(self, note):
        """
        example usage:
            my_note = Note(Content="This is my cool note")
            note_store.create_note(my_note)
        """
        session = Session(self.engine)
        session.add(note)
        session.commit()
        session.close()


    def update_note(self, updated_note):
        """
        example usage:
            update_me = Note(Id=12, Content="This note has been updated")
            note_store.update_note(update_me)
        """
        session = Session(self.engine)
        session.query(Note).filter(Note.Id == updated_note.Id) \
            .update({Note.Content: updated_note.Content})
        session.commit()
        session.close()


    def delete_note(self, delete_note):
        """
        This really only needs the id attached to the note. the content
        can be missing

        example usage:
            delete_me = Note(Id=12, Content="This note has been updated")
            note_store.delete_note(delete_me)
        """
        session = Session(self.engine)
        session.query(Note).filter(Note.Id == delete_note.Id).delete()
        session.commit()