import pandas as pd

from assets.config import YAML_COLUMNS_FILENAME
from services.logger import logger
from utils.column_lists import read_colums_yaml

from typing import Union


def read_excel_input_file(file_to_ingest: str) -> pd.DataFrame:
    """Esta función lee un archivo Excel definido en el parámetro `file_to_ingest`, y devuelve un DataFrame de Pandas, que luego será procesado, para poder manipular el inventario en una base de datos (inicialmente local).

    Args:
        file_to_ingest (str): nombre del archivo Excel a transformar desde Excel hacia un DataFrame de Pandas

    Returns:
        pd.DataFrame: DataFrame de Pandas con el archivo Excel ya cargado
    """
    # imports
    import os
    # setup
    input_loc = os.path.join(os.getcwd(), "inputs", file_to_ingest)
    # exec
    # reading file
    with open(file=input_loc, mode="rb") as file:
        pdf = pd.read_excel(io=file, sheet_name=0)
    # wrap up
    if not pdf.empty:
        logger.debug(f"Ingested inventory DataFrame:\n{pdf}")
        return pdf
    else:
        return False


def check_columns_on_file(ingested_pdf: pd.DataFrame, column_list: list) -> bool:
    """Esta función revisa que las columnas requeridas en la lista `column_list` sean exactamente iguales a las columnas que se encuentran en el DataFrame de Pandas ingestado previamente, `ingested_pdf`. Esta comprobación se realiza aplicando dos chequeos:

    1. Se revisan la cantidad de columnas que existen en el DataFrame y en la lista de columnas requeridas. Si la cantidad es distinta, la función sale con valor `False`.
    2. Se revisa columna a columna que el nombre exista en el DataFrame. Si algún nombre no existe en el Excel, la función sale con valor `False`.
    3. Si ambos chequeos pasan exitosamente, la función retorna `True`.

    Args:
        ingested_pdf (pd.DataFrame): DataFrame de Pandas con el Excel cargado previamente
        column_list (list): listado de columnas requeridas de inventario

    Returns:
        bool: `True` o `False` dependiendo de los chequeos descritos
    """
    # imports
    from assets.config import INVENTORY_INPUT_COL_LIST
    # setup
    requested_cols = column_list[INVENTORY_INPUT_COL_LIST]
    # exec
    ## check if number of columns is equal on ingestion and requisite
    cols_on_ingested_pdf = ingested_pdf.shape[1]
    cols_on_requested_list = len(requested_cols)
    logger.debug(cols_on_ingested_pdf)
    logger.debug(cols_on_requested_list)
    check_len_columns = cols_on_requested_list == cols_on_ingested_pdf
    if not check_len_columns:
        return False
    ## check if all requested columns are in ingested pdf
    logger.debug(ingested_pdf.columns)
    logger.debug(requested_cols)
    for column in requested_cols:
        if column not in ingested_pdf.columns:
            return False
    # wrap up
    logger.info("Ingested inventory file looks good. Proceeding...")
    return True


def ingestion_orchestration(file_to_ingest: str = None) -> Union[bool, pd.DataFrame]:
    """Esta función orquesta el proceso de ingesta del Excel de inventario. Ejecuta dos procesos en serie, comprobando en el camino si los resultados son correctos.

    Primero, ingesta el archivo Excel de inventario. Si hay algún error en la ingesta, retorna `False`.

    Luego, ejecuta la comprobación de columnas. Si hay algún problema en el chequeo, retorna `False`.

    Si la ejecución es correcta, retornará el DataFrame de Pandas ingestado.

    Args:
        file_to_ingest (str, optional): Nombre de archivo del archivo Excel a ingestar. Su valor por defecto es None.

    Returns:
        Union[bool, pd.DataFrame]: Si la ejecución es correcta, retorna un DataFrame de Pandas. Si la ejecución no es correcta, retorna `False`.
    """
    # imports
    # setup
    ## NOTE: hardcoded input file for testing purposes
    if file_to_ingest is None:
        TEST_FILE = "inventario-test.xlsx"
        logger.debug(f"Reading test file, '{TEST_FILE}'. Bear in mind, this is strictly for testing purposes")
        file_to_ingest = TEST_FILE
    # exec
    logger.info("Ingesting inventory Excel file...")
    ingested_pdf = read_excel_input_file(file_to_ingest=file_to_ingest)
    if ingested_pdf is False:
        logger.error("An error ocurred while ingesting the inventory file.\nPlease review and try again.")
        return False
    logger.info("Checking if the file is correctly formatted...")
    check_cols = check_columns_on_file(ingested_pdf=ingested_pdf, column_list=read_colums_yaml(file_name=YAML_COLUMNS_FILENAME))
    if not check_cols:
        logger.error("An error occurred while reading the inventory file.\nPlease review and try again.")
        return False
    # wrap up
    return ingested_pdf
