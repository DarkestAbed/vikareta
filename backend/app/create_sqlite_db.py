import sqlite3
import os

from lib.exceptions import DatabaseDoesNotExist
from services.logger import logger


def check_db_existence(db_file: str, create_db: bool = False) -> bool:
    """_summary_

    Args:
        db_file (str): _description_
        create_db (bool, optional): _description_. Defaults to False.

    Raises:
        ValueError: _description_

    Returns:
        bool: _description_
    """
    db_loc = os.path.join(os.getcwd(), "assets", db_file)
    logger.debug(db_loc)
    if os.path.exists(db_loc):
        logger.info(f"SQLite database '{db_loc}' exists")
        return True
    else:
        logger.error(f"Database file '{db_loc}' does not exists")
        if create_db:
            logger.warn("Database creation was requested, beware")
            logger.info(f"Creating SQLite database '{db_loc}'...")
            connection = sqlite3.connect(database=db_loc)
            logger.info("Database was successfully created.")
            connection.close()
            return True
        else:
            logger.exception("Database file does not exists and creation was not requested")
            raise DatabaseDoesNotExist(file=db_file)


def connect_to_sqlite_db(db_file: str) -> sqlite3.Connection:
    """_summary_

    Args:
        db_file (str): _description_

    Raises:
        Exception: _description_
        DatabaseDoesNotExist: _description_

    Returns:
        sqlite3.Connection: _description_
    """
    db_loc = os.path.join(os.getcwd(), "assets", db_file)
    logger.debug(db_loc)
    if os.path.exists(db_loc):
        try:
            connection = sqlite3.connect(database=db_loc)
            return connection
        except Exception as e:
            raise Exception(e)
    else:
        logger.error(f"Database file '{db_loc}' does not exists")
        logger.exception("Raising 'DatabaseDoesNotExist' error")
        raise DatabaseDoesNotExist(file=db_file)
