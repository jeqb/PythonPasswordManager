from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session(db_directory='', echo=False):
    """ Create an engine & session to the database. db_directory is the
    database directory on the machine """
    
    if db_directory == '':
        db_directory = Path.cwd() / 'database.db'
        db_directory = str(db_directory)

    connection_string = 'sqlite:///' + db_directory

    engine = create_engine(connection_string)

    Session = sessionmaker()
    Session.configure(bind=engine)

    return Session()