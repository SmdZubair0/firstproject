
"""
This file is to create all files and folder required
"""

import os
from pathlib import Path    # ensures the correct format of path in various os

# files to create
list_of_files = {

    ".github/workflows/.gitkeep", # gitkeep is a dummpy file (not to upload empty file)
    # workflow is for CI/CD

    # src represents entire source code
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipline.py",
    "src/utils/__init__.py"
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception",

    
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.config",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb" # for doing experiments
}

for filepath in list_of_files: # for each file
    filepath = Path(filepath)  # change to valid path

    filedir, filename = os.path.split(filepath)  # divide directory name and path name

    if filedir != "":   # if directory name is valid
        os.makedirs(filedir,exist_ok=True)  # create this directory 

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  # if path is valid and path exists
        with open(filepath, "w") as f:  # create file
            pass