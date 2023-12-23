from pandas import DataFrame
from app.ingest_excel_inventory import ingestion_orchestration
from services.logger import logger


def test_orchestration_returns_not_false():
    logger.critical(msg="test: orchestration returns not false")
    result_process = ingestion_orchestration()
    assert result_process is not False


def test_orchestration_returns_pandas_dataframe():
    logger.critical(msg="test: orchestration returns pandas dataframe")
    result_process = ingestion_orchestration()
    assert isinstance(result_process, DataFrame)
