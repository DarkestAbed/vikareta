import sqlite3

from backend.app.local.create_sqlite_db import connect_to_sqlite_db
from backend.assets.config import TEST_SQLITE_DB_PATH, TEST_SQLITE_DB_PATH_WRONG
from backend.lib.exceptions import DatabaseDoesNotExist
from backend.services.logger import Logger

logger: Logger = Logger()


def test_connect_to_db():
    logger.logger.critical(msg="test: connect to db")
    result = connect_to_sqlite_db(db_file=TEST_SQLITE_DB_PATH)
    assert isinstance(result, sqlite3.Connection)


def test_raise_valueerror_when_path_to_db_is_wrong():
    logger.logger.critical(msg="test: raise ValueError when path to db is wrong")
    try:
        result = connect_to_sqlite_db(db_file=TEST_SQLITE_DB_PATH_WRONG)
    except DatabaseDoesNotExist as e:
        logger.logger.exception(e)
        logger.logger.debug(e.__class__.__name__)
        result = False
    except Exception as e:
        logger.logger.exception(e)
        logger.logger.debug(e.__class__.__name__)
        result = None
    assert result is False
