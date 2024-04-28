from backend.assets.config import YAML_COLUMNS_FILENAME, INVENTORY_INPUT_COL_LIST
from backend.services.logger import Logger
from backend.utils.column_lists import read_colums_yaml

logger: Logger = Logger(logger_name="test_input-reads")


def test_read_input_yaml():
    logger.logger.critical(msg="test: read input yaml")
    result_read = read_colums_yaml(file_name=YAML_COLUMNS_FILENAME)
    assert result_read is not False


def test_read_input_yaml_returns_dict():
    logger.logger.critical(msg="test: read input yaml returns dict")
    result_read = read_colums_yaml(file_name=YAML_COLUMNS_FILENAME)
    assert isinstance(result_read, dict)


def test_read_input_yaml_contains_input_xlsx_key():
    logger.logger.critical(msg="test: read input yaml contains input xlsx keys")
    result_read = read_colums_yaml(file_name=YAML_COLUMNS_FILENAME)
    assert result_read.get(INVENTORY_INPUT_COL_LIST, None) is not None


def test_read_input_yaml_input_xlsx_key_value_is_list():
    logger.logger.critical(msg="test: read input yaml input xlsx key value is list")
    result_read = read_colums_yaml(file_name=YAML_COLUMNS_FILENAME)
    assert isinstance(result_read[INVENTORY_INPUT_COL_LIST], list)
