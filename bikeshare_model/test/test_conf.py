import os, sys
from config import core
from pathlib import Path

def test_config_file_exist():
    assert Path.is_file(core.CONFIG_FILE_PATH)

def test_data_file_exist():
    data_file_path = os.path.join(os.path.join(core.DATASET_DIR, 'bike-rental-dataset.csv'))
    assert os.path.exists(data_file_path)

