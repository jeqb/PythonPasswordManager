from .Entry import Entry

from sqlalchemy.orm import Session

class EntryStore:
    """
    Provides the CRUD functionality for Password Entries
    """
    def __init__(self, engine):
        """
        example:
            from sqlalchemy import create_engine
            engine = create_engine('sqlite:///database.db')
            entry_store = EntryStore(engine)
        """
        self.engine = engine


    def get_entries(self):
        """
        example usage:
            results = entry_store.get_entries()

            for row in results:
                print(row.Id)
                print(row.Username)
                print(row.Email)
                print(row.Password)
                print(row.Category)
                print(row.Note)
        """
        session = Session(self.engine)
        result = session.query(Entry).all()
        session.close()

        return result


    def get_entry_by_id(self, id):
        """
        example usage:
            entry = entry_store.get_entry_by_id(2)
            print(entry.Id)
            print(entry.Username)
            print(entry.Email)
            print(entry.Password)
        """
        session = Session(self.engine)
        result = session.query(Entry).filter_by(Id=id).first()
        session.close()

        return result


    def create_entry(self, entry):
        """
        example usage:
            new_entry = Entry(
                Username="Test Username",
                Email="Test email",
                Password="Test password",
                Category="Test Category",
                Note="Test Note"
                )

            entry_store.create_entry(new_entry)
        """
        session = Session(self.engine)
        session.add(entry)
        session.commit()
        session.close()


    def update_entry(self, updated_entry):
        """
        example usage:
            updated_entry = Entry(
                Id=1,
                Username="Updated Username",
                Email="Test email",
                Password="Test password",
                Category="Test Category",
                Note="Test Note"
                )

            entry_store.update_entry(new_entry)
        """
        update_dict = {
            Entry.Id: updated_entry.Id,
            Entry.Website: updated_entry.Website,
            Entry.Username: updated_entry.Username,
            Entry.Email: updated_entry.Email,
            Entry.Password: updated_entry.Password,
            Entry.Category: updated_entry.Category,
            Entry.Note: updated_entry.Note
        }

        session = Session(self.engine)
        session.query(Entry).filter(Entry.Id == updated_entry.Id) \
            .update(update_dict)
        session.commit()
        session.close()


    def delete_entry(self, delete_entry):
        """
        only the Id is needed on the object

        example usage:
            new_entry = Entry(
                Id=1,
                Username="Updated Username",
                Email="Test email",
                Password="Test password",
                Category="Test Category",
                Note="Test Note"
                )
        """
        session = Session(self.engine)
        session.query(Entry).filter(Entry.Id == delete_entry.Id).delete()
        session.commit()

    
    def search_entry_by_website(self, website_string):
        """
        Given a string of text, search for it in the "Website" column
        using "LIKE" + wildcard operators

        example usage:
            search_string = "Some Note Text"
            search_results = entry_store.search_enry_by_website(search_string)
        """
        wildcard_search = '%' + website_string + '%'

        session = Session(self.engine)
        results = session.query(Entry).filter(Entry.Website.like(wildcard_search)).all()
        session.close()

        return results


    def search_entry_by_website_and_category(self, website_string, category_string):
        """
        Given a string of text, search for it in the "Website" column
        using "LIKE" + wildcard operators
        
        example usage:
            search_string = "Some Note Text"
            search_results = entry_store.search_enry_by_website(search_string)
        """
        wildcard_search = '%' + website_string + '%'

        session = Session(self.engine)
        results = session.query(Entry).filter(
            Entry.Website.like(wildcard_search),
            Entry.Category == category_string
            ).all()
        session.close()

        return results