import pytest

from backend.app.common.process_ingested_data import define_quantities_on_ingested_inventory
from backend.services.logger import Logger

logger: Logger = Logger(logger_name="test_process-ingested-data")


@pytest.mark.skip(reason="not developed yet")
def test_check_all_items_have_quantities():
    logger.logger.critical(msg="test: check all ingested items have quantities assigned")
    result = define_quantities_on_ingested_inventory()
    assert result is not None
