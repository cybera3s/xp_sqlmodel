from sqlmodel import SQLModel, create_engine

# internal
from models.blog import *  # noqa


sqlite_file_name = "sqlite3.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# It is an object that handles the communication with the database
engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
