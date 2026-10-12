import os
from pathlib import Path

folder_name="src"

list_of_files=[
    f"{folder_name}/__init__.py",
    f"{folder_name}/components/__init__.py",
    f"{folder_name}/components/data_ingestion.py",
    f"{folder_name}/components/data_validation.py",
    f"{folder_name}/components/data_transformation.py",
    f"{folder_name}/components/model_trainer.py",
    f"{folder_name}/components/model_evaluation.py",
    f"{folder_name}/components/model_pusher.py",
    f"{folder_name}/configuration/__init__.py",
    f"{folder_name}/configuration/mongo_db_connection.py",
    f"{folder_name}/configuration/aws_connection.py",
    f"{folder_name}/cloud_storage/__init__.py",
    f"{folder_name}/cloud_storage/aws_storage.py",
    f"{folder_name}/data_access/__init__.py",
    f"{folder_name}/data_access/proj1_data.py",
    f"{folder_name}/constants/__init__.py",
    f"{folder_name}/entity/__init__.py",
    f"{folder_name}/entity/config_entity.py",
    f"{folder_name}/entity/artifact_entity.py",
    f"{folder_name}/entity/estimator.py",
    f"{folder_name}/entity/s3_estimator.py",
    f"{folder_name}/exception/__init__.py",
    f"{folder_name}/logger/__init__.py",
    f"{folder_name}/pipeline/__init__.py",
    f"{folder_name}/pipeline/training_pipeline.py",
    f"{folder_name}/pipeline/prediction_pipeline.py",
    f"{folder_name}/utils/__init__.py",
    f"{folder_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml"
]

for file in list_of_files:
    filepath=Path(file)
    file_dir, file_name=os.path.split(filepath)
    if file_dir!="":
        os.makedirs(file_dir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"{file} already exists and is not empty. Skipping file creation.")