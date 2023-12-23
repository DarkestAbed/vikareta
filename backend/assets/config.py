from logging import DEBUG, INFO


# operation values
DATE_FMT = "%Y%m%d"
TIMESTAMP_FMT = "%Y%m%d-%H%M%S.%f"
LOGGING_FILE_LEVEL = DEBUG
LOGGING_CONS_LEVEL = DEBUG
LOGGING_FMT = "%(asctime)s || %(filename)s - %(funcName)s || :: %(levelname)s :: %(message)s"
YAML_COLUMNS_FILENAME = "columns.yml"
INVENTORY_INPUT_COL_LIST = "input_xlsx"
# test values
TEST_SQLITE_DB_PATH = "test.db"
TEST_SQLITE_DB_PATH_WRONG = "test_wrong.db"
TEST_FILE = "inventario-test.xlsx"
TEST_FILE_ERROR = "inventario-test-erroneo.xlsx"
