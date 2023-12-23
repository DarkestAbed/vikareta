import os
import yaml

def read_colums_yaml(file_name: str) -> dict:
    # imports
    # setup
    yaml_dir = os.path.join(os.getcwd(), "assets")
    yaml_full_loc = os.path.join(yaml_dir, file_name)
    # exec
    ## check if file exists
    if not os.path.exists:
        raise FileNotFoundError
    ## read selected yaml file
    with open(file=yaml_full_loc, mode="r") as file:
        columns_dict = yaml.safe_load(stream=file)
    # wrap up
    return columns_dict
