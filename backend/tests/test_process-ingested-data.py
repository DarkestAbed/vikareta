import pytest

from pandas import DataFrame

from backend.app.common.process_ingested_data import load_data_from_inventory_db
from backend.assets.config import TEST_SQLITE_DB_PATH, TEST_TABLE_NAME
from backend.services.logger import Logger

logger: Logger = Logger(logger_name="test_process-ingested-data")


def test_load_data_from_inventory():
    logger.logger.critical(msg="test: extracting data from inventory table")
    result = load_data_from_inventory_db(db_file=TEST_SQLITE_DB_PATH, table_name=TEST_TABLE_NAME)
    assert isinstance(result, DataFrame)


@pytest.mark.skip(reason="not developed yet")
def test_check_if_duplicates_on_inventory():
    pass


@pytest.mark.skip(reason="not developed yet")
def test_consolidate_inventory():
    pass
