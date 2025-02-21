import os
from pathlib import Path
import logging

# logging string - it will create folders and all, also logs everything during the process
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "kidneyDiseaseClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "main.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "settings/settings.py",
    "test/test.py"
]

for filePath in list_of_files:
    filePath = Path(filePath)
    folderName, fileName = os.path.split(filePath)
    
    if folderName != "":
        os.makedirs(folderName, exist_ok=True)
        logging.info(f"Creating directory; {folderName} for the file: {fileName}")
        
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath) == 0):
        with open(filePath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filePath}")
            
    else:
        logging.info(f"{filePath} is already exists")
        
    