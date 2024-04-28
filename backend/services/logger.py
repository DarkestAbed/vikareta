import logging
import os

from datetime import datetime
from typing import NoReturn

from backend.assets.config import DATE_FMT, LOGGING_FILE_LEVEL, LOGGING_CONS_LEVEL, LOGGING_FMT, PROJ_PATH


class Logger:
    def __init__(self) -> NoReturn:
        # general setup
        date_dt: str = datetime.strftime(datetime.now(), DATE_FMT)
        # logging config
        ## logger
        self.logger: logging.Logger = logging.getLogger("console_output")
        ## console logger
        console_log: logging.StreamHandler = logging.StreamHandler()
        ## file logger
        log_path: str = os.path.join(PROJ_PATH, "output", f"{date_dt}-execution.log")
        file_log: logging.FileHandler = logging.FileHandler(filename=log_path, mode="a", encoding="latin-1", delay=False)
        ## set levels
        self.logger.setLevel(logging.DEBUG)
        console_log.setLevel(LOGGING_CONS_LEVEL)
        file_log.setLevel(LOGGING_FILE_LEVEL)
        ## set up formatter
        formatter: logging.Formatter = logging.Formatter(LOGGING_FMT)
        console_log.setFormatter(formatter)
        file_log.setFormatter(formatter)
        ## add console log to handler
        self.logger.addHandler(console_log)
        self.logger.addHandler(file_log)
        return None
