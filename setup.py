from setuptools import setup, find_packages
from typing import List

# Project Setup Variables
PROJECT_NAME = "Housing Price Prediction Model"
PROJECT_VERSION = "0.0.1"
AUTHOR = "Mujeeb Subhani"
DESCRIPTION = "This project is to predict housing price of California"
PACKAGES = ["HOUSING"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list() -> List[str]:
    # It returns a list of requirements, placed in requirements.txt
    with open (REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()



setup(
   name = PROJECT_NAME,
   version = PROJECT_VERSION,
   author = AUTHOR,
   description=DESCRIPTION,
   packages=find_packages(),
   install_requires = get_requirements_list(),
)

