from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = 'sqlite://///Users/danyaaleksandrov/Desktop/evraz_project2/user.db'

