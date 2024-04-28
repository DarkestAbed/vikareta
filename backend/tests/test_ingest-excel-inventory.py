from backend.app.local.ingest_excel_inventory import read_excel_input_file, check_columns_on_file
from backend.assets.config import YAML_COLUMNS_FILENAME, INVENTORY_INPUT_COL_LIST, TEST_FILE, TEST_FILE_ERROR
from backend.services.logger import Logger
from backend.utils.column_lists import read_colums_yaml

logger: Logger = Logger(logger_name="test_ingest-excel-inventory")


def test_ingest_excel():
    logger.logger.critical(msg="test: ingest excel")
    result_ingestion = read_excel_input_file(file_to_ingest=TEST_FILE)
    assert result_ingestion is not False


def test_check_filter_of_input_cols():
    logger.logger.critical(msg="test: check filter of input cols")
    result_ingestion = read_colums_yaml(file_name=YAML_COLUMNS_FILENAME)[INVENTORY_INPUT_COL_LIST]
    assert isinstance(result_ingestion, list)


def test_columns_are_correct_on_ingested_file():
    logger.logger.critical(msg="test: columns are correct on ingested file")
    result_ingestion = check_columns_on_file(ingested_pdf=read_excel_input_file(file_to_ingest=TEST_FILE), column_list=read_colums_yaml(file_name=YAML_COLUMNS_FILENAME))
    assert result_ingestion is not False


def test_columns_are_not_correct_on_ingested_file():
    logger.logger.critical(msg="test: columns are not correct on ingested file")
    result_ingestion = check_columns_on_file(ingested_pdf=read_excel_input_file(file_to_ingest=TEST_FILE_ERROR), column_list=read_colums_yaml(file_name=YAML_COLUMNS_FILENAME))
    assert result_ingestion is False
