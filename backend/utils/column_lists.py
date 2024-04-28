import os
import yaml

from backend.assets.config import PROJ_PATH


def read_colums_yaml(file_name: str) -> dict:
    # imports
    # setup
    yaml_full_loc: str = os.path.join(PROJ_PATH, "assets", file_name)
    # exec
    ## check if file exists
    if not os.path.exists:
        raise FileNotFoundError
    ## read selected yaml file
    with open(file=yaml_full_loc, mode="r") as file:
        columns_dict: dict = yaml.safe_load(stream=file)
    # wrap up
    return columns_dict
