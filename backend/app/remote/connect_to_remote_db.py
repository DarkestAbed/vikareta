import pandas as pd

from backend.app.local.ingest_excel_inventory import ingestion_orchestration


def define_quantities_on_ingested_inventory(input_data: pd.DataFrame) -> list[tuple]:
    validation_list: list[tuple] = []
    return validation_list