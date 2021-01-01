from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Connection

from Common.Constants import DECRYPTED_DATABASE_NAME


def create_connection(db_directory: str='', echo: bool=False) -> Connection:
    """ Creates a database and the connection to it. db_directory is the
    database directory on the machine """
    
    if db_directory == '':
        db_directory = Path.cwd() / DECRYPTED_DATABASE_NAME
        db_directory = str(db_directory)

    connection_string = 'sqlite:///' + db_directory

    engine = create_engine(connection_string)

    return engine.connect()


def create_database_engine(db_directory: str='', echo: bool=False):
    """ Creates a database engine. db_directory is the
    database directory on the machine """
    
    if db_directory == '':
        db_directory = Path.cwd() / DECRYPTED_DATABASE_NAME
        db_directory = str(db_directory)

    connection_string = 'sqlite:///' + db_directory

    engine = create_engine(connection_string)

    return engine


def create_tables(declarative_base_instance, engine):
    """
    Creates the database table schema given an instance
    of the declarative_base and the engine
    """

    declarative_base_instance.metadata.create_all(engine)