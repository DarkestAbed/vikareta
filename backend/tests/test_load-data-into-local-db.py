# backend/tests/test_load-data-into-local-db.py
import pytest

from backend.app.local.ingest_excel_inventory import ingestion_orchestration
from backend.app.local.sink_into_db import check_local_dest_table, data_load_into_db
from backend.assets.config import TEST_SQLITE_DB_PATH, TEST_TABLE_NAME, TEST_FILE_ERROR
from backend.lib.exceptions import DataInsertionError
from backend.services.logger import Logger
from backend.utils.column_lists import read_colums_yaml

logger: Logger = Logger(logger_name="test_load-data-into-local-db")


def test_check_dest_table():
    logger.logger.critical(msg="test: check destination table on local db")
    result = check_local_dest_table(db_file=TEST_SQLITE_DB_PATH, table_name=TEST_TABLE_NAME)
    assert result is True


def test_write_data_into_db():
    logger.logger.critical(msg="test: write data into local db")
    input_data = ingestion_orchestration(file_to_ingest=None)
    result = data_load_into_db(input_data=input_data, db_file=TEST_SQLITE_DB_PATH, table_name=TEST_TABLE_NAME)
    assert result is None

def test_write_wrong_data_into_db():
    logger.logger.critical(msg="test: write wrong data into local db")
    with pytest.raises(DataInsertionError) as e:
        input_data = ingestion_orchestration(file_to_ingest=TEST_FILE_ERROR)
        if input_data is False:
            raise DataInsertionError
        result = data_load_into_db(input_data=input_data, db_file=TEST_SQLITE_DB_PATH, table_name=TEST_TABLE_NAME)
