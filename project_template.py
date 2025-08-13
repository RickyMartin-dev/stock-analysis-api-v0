# Imports
import os
from pathlib import Path
import logging

# Define Logging Format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# specify files to create
list_of_files = [
    ".env", # purely for local development
    ".github/workflows/.gitkeep", # preliminary files for github actions
    "requirements.txt", # for package information 
    "Dockerfile",
    "tests/__init__.py",
    "src/__init__.py", # to import files
    "src/config.py", # to import files
    "src/utils.py", # utilies aka. repeated function
    "src/main.py", # main API logic
    "src/rate_limit.py", # rate limiting logic
    "src/schema.py", # schema for api
    "src/clients.py", # logic to define client functions
    "src/logging_setup.py", # logging setup
]

# Go through list and create folders/files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # logic for directory
    if filedir != "":
        # create directory
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # Create the files
    # check if file exists I do not want to replace
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else: # if file already exists
        logging.info(f"{filename} already exists")