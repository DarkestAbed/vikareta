# backend/app/local/sink_into_db.py
import pandas as pd

from datetime import datetime
from os.path import join as path_join
from sqlite3 import Connection, Cursor
from typing import Any

from backend.app.local.create_sqlite_db import connect_to_sqlite_db
from backend.assets.config import PROJ_PATH, TEST_TABLE_DTYPES, DATE_DB_FMT
from backend.lib.exceptions import DataInsertionError, UnknownError
from backend.lib.sqlite_db import SQLiteDB
from backend.services.logger import Logger

logger: Logger = Logger(logger_name="sink_into_db")


def check_local_dest_table(db_file: str, table_name: str) -> bool:
    SQL_LIST_TABLES_CMD: str = "SELECT name FROM sqlite_master WHERE type = 'table'"
    connection: Connection = connect_to_sqlite_db(db_file=db_file)
    cursor: Cursor = connection.execute(SQL_LIST_TABLES_CMD)
    results: list[Any] = cursor.fetchall()
    return_value: bool = False
    logger.logger.debug(results)
    if len(results) < 1:
        logger.logger.critical("Development database is empty")
        logger.logger.info("Creating tables at run time...")
        db: SQLiteDB = SQLiteDB(db_file=f"sqlite:///{path_join(PROJ_PATH, "assets", db_file)}")
        results: list[Any] = db.execute_query(q=SQL_LIST_TABLES_CMD)
    else:
        logger.logger.info("Database already populated. Proceeding...")
    for table in results:
        logger.logger.debug(f"Item: {table} ; type: {type(table)}")
        if table_name == table[0]:
            return_value = True
            break
        else:
            next
    return return_value


def data_load_into_db(input_data: pd.DataFrame, db_file: str, table_name: str) -> None:
    db: SQLiteDB = SQLiteDB(db_file=f"sqlite:///{path_join(PROJ_PATH, "assets", db_file)}")
    column_mapper: dict = {
        "nombre": "name",
        "cantidad": "quantity",
        "costo": "cost",
        "precio": "price",
        "fecha": "purchased_date",
    }
    upload_data: pd.DataFrame = input_data.rename(columns=column_mapper)
    upload_data["added_date"] = datetime.now()
    try:
        result_int = upload_data.to_sql(
            name=table_name,
            con=db.engine,
            if_exists="replace",
            index=False,
            dtype=TEST_TABLE_DTYPES,
            chunksize=100,
            method="multi",
        )
    except ValueError:
        raise DataInsertionError
    except Exception:
        logger.logger.exception(msg="Unknown exception found. Terminating.")
        raise UnknownError
    logger.logger.debug(f"Affected rows: {result_int}")
    if not result_int is None and result_int > 0:
        return None
    else:
        raise DataInsertionError


if __name__ == "__main__":
    from backend.assets.config import TEST_SQLITE_DB_PATH, TEST_TABLE_NAME
    from backend.app.local.ingest_excel_inventory import ingestion_orchestration
    data: pd.DataFrame = ingestion_orchestration(file_to_ingest=None)
    data_load_into_db(db_file=TEST_SQLITE_DB_PATH, table_name=TEST_TABLE_NAME, input_data=data)
else:
    pass
