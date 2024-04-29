# backend/app/common/process_ingested_data.py
import pandas as pd

from sqlalchemy import Engine

from backend.lib.sqlite_db import SQLiteDB
from backend.services.logger import Logger
from backend.utils.local_sqlite_location import return_sqlite_db_uri

logger: Logger = Logger(logger_name="process_ingested_data")


def load_data_from_inventory_db(db_file: str, table_name: str = "inventory") -> pd.DataFrame:
    db_uri: str = return_sqlite_db_uri(db_file=db_file)
    conn: SQLiteDB = SQLiteDB(db_file=db_uri)
    engine: Engine = conn.engine
    inventory_pdf: pd.DataFrame = pd.read_sql_table(table_name=table_name, con=engine, index_col="id")
    logger.logger.debug(f"Inventory DataFrame data:\n{inventory_pdf}")
    return inventory_pdf


def consolidate_inventory():
    pass
