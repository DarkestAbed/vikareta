import logging
import os

from datetime import datetime
from assets.config import DATE_FMT, LOGGING_FILE_LEVEL, LOGGING_CONS_LEVEL, LOGGING_FMT


# general setup
date_dt = datetime.strftime(datetime.now(), DATE_FMT)
# logging config
## logger
logger = logging.getLogger("console_output")
## console logger
console_log = logging.StreamHandler()
## file logger
log_path = os.path.join(os.getcwd(), "output", f"{date_dt}-execution.log")
file_log = logging.FileHandler(filename=log_path, mode="a", encoding="latin-1", delay=False)
## set levels
logger.setLevel(logging.DEBUG)
console_log.setLevel(LOGGING_CONS_LEVEL)
file_log.setLevel(LOGGING_FILE_LEVEL)
## set up formatter
formatter = logging.Formatter(LOGGING_FMT)
console_log.setFormatter(formatter)
file_log.setFormatter(formatter)
## add console log to handler
logger.addHandler(console_log)
logger.addHandler(file_log)
