from logging import DEBUG, INFO
from os.path import join as path_join
from sqlalchemy import Integer, String, Date

from backend.utils.project_location import check_proj_location


# path values
PROJ_PATH = path_join(check_proj_location(), "backend")
# operation values
DATE_FMT = "%Y%m%d"
DATE_DB_FMT = "%Y-%m-%d"
TIMESTAMP_FMT = "%Y%m%d-%H%M%S.%f"
LOGGING_FILE_LEVEL = DEBUG
LOGGING_CONS_LEVEL = DEBUG
LOGGING_FMT = "{ %(name)s } || %(asctime)s || %(filename)s - %(funcName)s (%(lineno)d) || :: %(levelname)s :: %(message)s"
YAML_COLUMNS_FILENAME = "columns.yml"
INVENTORY_INPUT_COL_LIST = "input_xlsx"
# test values
TEST_SQLITE_DB_PATH = "test.db"
TEST_SQLITE_DB_PATH_WRONG = "test_wrong.db"
TEST_FILE = "inventario-test.xlsx"
TEST_FILE_ERROR = "inventario-test-erroneo.xlsx"
TEST_TABLE_NAME = "inventory"
TEST_TABLE_DTYPES = {
    "name": String,
    "quantity": Integer,
    "cost": Integer,
    "price": Integer,
    "purchased_date": Date,
    "added_date": Date,
}
