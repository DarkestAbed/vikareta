import sqlite3

from app.create_sqlite_db import connect_to_sqlite_db
from assets.config import TEST_SQLITE_DB_PATH, TEST_SQLITE_DB_PATH_WRONG
from lib.exceptions import DatabaseDoesNotExist
from services.logger import logger


def test_connect_to_db():
    logger.critical(msg="test: connect to db")
    result = connect_to_sqlite_db(db_file=TEST_SQLITE_DB_PATH)
    assert isinstance(result, sqlite3.Connection)


def test_raise_valueerror_when_path_to_db_is_wrong():
    logger.critical(msg="test: raise ValueError when path to db is wrong")
    try:
        result = connect_to_sqlite_db(db_file=TEST_SQLITE_DB_PATH_WRONG)
    except DatabaseDoesNotExist as e:
        logger.exception(e)
        logger.debug(e.__class__.__name__)
        result = False
    except Exception as e:
        logger.exception(e)
        logger.debug(e.__class__.__name__)
        result = None
    assert result is False
