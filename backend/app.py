from app.ingest_excel_inventory import ingestion_orchestration
from services.logger import logger


def main():
    print("\n========================", flush=True)
    logger.info("Starting all processes...")
    ingestion_orchestration(file_to_ingest=None)
    logger.info("Wrapping up all processes...")
    print("========================\n", flush=True)


if __name__ == "__main__":
    main()