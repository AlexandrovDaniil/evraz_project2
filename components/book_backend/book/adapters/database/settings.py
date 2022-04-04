import os

from pydantic import BaseSettings


# class Settings(BaseSettings):
#     DB_URL: str = 'sqlite://///Users/danyaaleksandrov/Desktop/evraz_project2/book.db'

class Settings(BaseSettings):
    @property
    def DB_URL(self):
        PG_USER = 'suuser'
        PG_PASSWORD = 'suuser'
        PG_DBNAME = 'booksdb'
        PG_HOST = os.getenv('POSTGRES_DB_HOST', 'localhost')
        PG_PORT = '5432'

        return f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DBNAME}"
