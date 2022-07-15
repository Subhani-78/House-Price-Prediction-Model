import yaml
from housing.exception import CodeException
import os, sys

def read_yaml_file(file_path:str) -> dict :
    try:
        with open (file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CodeException(e, sys) from e