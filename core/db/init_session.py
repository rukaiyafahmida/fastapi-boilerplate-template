from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.fastapi.logger import logger

load_dotenv()


DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_DRIVER=os.getenv("DB_DRIVER")
DB_NAME=os.getenv("DB_NAME")
PROJECT_DATABASE=os.getenv("DB_NAME")

class DataBaseHandler:
    """
    A class to represent a Handler for Database.
    ...
    Attributes
    ----------
    base_url : str
        base url of the server

    Methods
    -------
    create_db(db_name: str) -> str:
        Creates the database with the given name and returns the database URL.
        If the database already exists, it returns the URL without creating a new database.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the handler object.
        """
        self.base_url = f"{DB_NAME}+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/"

    def create_db(self, db_name: str):
        """
        Creates the database with the given name and returns the database URL.
        If the database already exists, it returns the URL without creating a new database.
        Args:
            db_name (str): Name of the database to be created.

        Returns:
            str: URL of the created database.

        Raises:
            Exception: If any error occurs while creating the database or getting the URL,
            the error message is logged using the logger.

        """
        url = f"{self.base_url}{db_name}"
        try:
            if not database_exists(url):
                create_database(url)
                logger.info("The database has been created.")
            return url

        except Exception as e:
            logger.error(f"Error get database url. Error: {e}")


handler = DataBaseHandler()
db_url = handler.create_db(os.getenv("PROJECT_DATABASE"))
engine = create_engine(db_url)
conn = engine.connect()
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

## Common Session for reading only 
session = SessionLocal()


def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def create_tables():
    Base.metadata.create_all(engine)
    print("created")
