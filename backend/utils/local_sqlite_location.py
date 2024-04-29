# backend/utils/local_sqlite_location.py
from os.path import join as path_join

from backend.assets.config import PROJ_PATH


def return_sqlite_db_uri(db_file: str) -> str:
    uri: str = f"sqlite:///{path_join(PROJ_PATH, "assets", db_file)}"
    return uri
