from .EncryptionCheck import EncryptionCheck

from sqlalchemy.orm import Session

class EncryptionCheckStore:
    """
    Provides CRUD functionality for the EncryptionCheck table
    """
    def __init__(self, engine):
        """
        example:
            from sqlalchemy import create_engine
            engine = create_engine('sqlite:///database.db')
            encryption_store = EncryptionCheckStore(engine)
        """
        self.engine = engine


    def get_row_by_id(self, id):
        """
        example usage:
            entry = encryption_store.get_row_by_id(1)
            print(entry.Id)
            print(entry.EncryptionMessage)
        """
        session = Session(self.engine)
        result = session.query(EncryptionCheck).filter_by(Id=id).first()
        session.close()

        return result


    def create_row(self, row):
        """
        example usage:
            new_entry = EncryptionCheck(
                EncryptionMessage = "SDFSDFHKJSDFKJHFSDKJHFSDKJ"
                )

            encryption_store.create_entry(new_entry)
        """
        session = Session(self.engine)
        session.add(row)
        session.commit()
        session.close()


    def update_row(self, updated_row):
        """
        example usage:
            updated_entry = EncryptionCheck(
                Id=1,
                EncryptionMessage = "ififififififkerkrjerk"
                )

            encryption_store.update_entry(updated_entry)
        """
        update_dict = {
            EncryptionCheck.Id: updated_row.Id,
            EncryptionCheck.EncryptionMessage: updated_row.EncryptionMessage,
        }

        session = Session(self.engine)
        session.query(EncryptionCheck).filter(EncryptionCheck.Id == updated_row.Id) \
            .update(update_dict)
        session.commit()
        session.close()


    def delete_row(self, delete_row):
        """
        only the Id is needed on the object

        example usage:
            delete_me = EncryptionCheck(
                Id=1,
                )
        """
        session = Session(self.engine)
        session.query(EncryptionCheck).filter(EncryptionCheck.Id == delete_row.Id).delete()
        session.commit()
        session.close()