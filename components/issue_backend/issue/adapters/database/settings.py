import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    @property
    def DB_URL(self):
        PG_USER = 'suuser'
        PG_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'suuser')
        PG_DBNAME = 'issuesdb'
        PG_HOST = os.getenv('POSTGRES_DB_HOST', 'localhost')
        PG_PORT = '5432'

        return f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DBNAME}"
