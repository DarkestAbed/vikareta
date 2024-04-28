import pytest

from backend.app.local.create_sqlite_db import check_db_existence
from backend.assets.config import TEST_SQLITE_DB_PATH, TEST_SQLITE_DB_PATH_WRONG, PROJ_PATH
from backend.lib.exceptions import DatabaseDoesNotExist
from backend.services.logger import Logger

logger: Logger = Logger(logger_name="test_create-sqlite-db")


def test_check_if_database_exists():
    logger.logger.critical(msg="test: check if db exists")
    result = check_db_existence(db_file=TEST_SQLITE_DB_PATH)
    assert result is True


def test_check_if_database_path_does_not_exists():
    logger.logger.critical(msg="test: check if database path does not exists")
    try:
        result = check_db_existence(db_file=TEST_SQLITE_DB_PATH_WRONG)
    except DatabaseDoesNotExist as e:
        logger.logger.exception(e)
        logger.logger.debug(e.__class__.__name__)
        result = False
    except Exception as e:
        logger.logger.exception(e)
        logger.logger.debug(e.__class__.__name__)
        result = None
    assert result is False


def test_check_if_database_gets_created_when_path_does_not_exists_and_is_requested():
    logger.logger.critical(msg="test: check if database gets created when path does not exists and db creation is requested")
    try:
        intermediate = check_db_existence(db_file=TEST_SQLITE_DB_PATH_WRONG, create_db=True)
    except ValueError:
        pass
    result = check_db_existence(db_file=TEST_SQLITE_DB_PATH_WRONG)
    assert result is True
    import os
    os.remove(path=os.path.join(PROJ_PATH, "assets", TEST_SQLITE_DB_PATH_WRONG))


def test_check_if_database_is_not_created_when_path_does_not_exists_and_is_not_requested():
    logger.logger.critical(msg="test: check if database is not created when path does not exists and db creation is not requested")
    try:
        intermediate = check_db_existence(db_file=TEST_SQLITE_DB_PATH_WRONG, create_db=False)
    except DatabaseDoesNotExist:
        result = False
    assert result is False
