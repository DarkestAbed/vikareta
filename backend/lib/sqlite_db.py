# backend/lib/sqlite_db.py
from datetime import date, datetime
from sqlalchemy import create_engine, text, Column, Integer, String, Date, CursorResult
from sqlalchemy.orm import declarative_base
from typing import Any

from backend.assets.config import DATE_DB_FMT
from backend.services.logger import Logger

logger: Logger = Logger(logger_name="sqlite_db")
Base: Any = declarative_base()


class SQLiteDB:
    class Inventory(Base):
        __tablename__: str = "inventory"
        id: Column = Column(name="id", type_=Integer, autoincrement=True, primary_key=True, nullable=False)
        name: Column = Column(name="name", type_=String, autoincrement=False, primary_key=False, nullable=False)
        quantity: Column = Column(name="quantity", type_=Integer, autoincrement=False, primary_key=False, nullable=False)
        cost: Column = Column(name="cost", type_=Integer, autoincrement=False, primary_key=False, nullable=False)
        price: Column = Column(name="price", type_=Integer, autoincrement=False, primary_key=False, nullable=False)
        purchase_date: Column = Column(name="purchase_date", type_=Date, autoincrement=False, primary_key=False, nullable=False)
        added_date: Column = Column(name="added_date", type_=Date, autoincrement=False, primary_key=False, nullable=True)

        def __init__(self, name: str, q: int, cost: int, price: int, purchased: date, added: date = None) -> None:
            self.name: str = name
            self.quantity: int = q
            self.cost: int = cost
            self.price: int = price
            self.purchase_date: date = purchased
            if added is None:
                self.added_date: date = datetime.strftime(self=datetime.now(), format=DATE_DB_FMT)
            else:
                self.added_date: date = datetime.strftime(self=added, format=DATE_DB_FMT)
            return None

    def __init__(self, db_file: str) -> None:
        logger.logger.debug(f"{db_file = }")
        self.engine = create_engine(url=db_file)
        logger.logger.debug(f"{self.engine = }")
        logger.logger.debug("Creating tables...")
        Base.metadata.create_all(self.engine)
        logger.logger.debug("Tables created!")
        return None
    
    def execute_query(self, q: str):
        with self.engine.connect() as connection:
            result: CursorResult = connection.execute(text(text=q)).all()
            connection.commit()
        logger.logger.debug(result)
        return result
