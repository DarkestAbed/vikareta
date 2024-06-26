from pandas import DataFrame
from backend.app.local.ingest_excel_inventory import ingestion_orchestration
from backend.services.logger import Logger

logger: Logger = Logger(logger_name="test_ingestion-orchestration")


def test_orchestration_returns_not_false():
    logger.logger.critical(msg="test: orchestration returns not false")
    result_process = ingestion_orchestration()
    assert result_process is not False


def test_orchestration_returns_pandas_dataframe():
    logger.logger.critical(msg="test: orchestration returns pandas dataframe")
    result_process = ingestion_orchestration()
    assert isinstance(result_process, DataFrame)
