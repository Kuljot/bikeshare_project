import os, sys
from pathlib import Path
from predict import pipeline_file_name, make_prediction


def test_pkl_file_exist():
    PKL_FILE_PATH=os.path.join('trained_models',Path(pipeline_file_name))
    assert os.path.exists(PKL_FILE_PATH)

def test_prediction():
    data_in = {'dteday': ['2012-11-6'], 'season': ['winter'], 'hr': ['6pm'], 'holiday': ['No'], 'weekday': ['Tue'],
               'workingday': ['Yes'], 'weathersit': ['Clear'], 'temp': [16], 'atemp': [17.5], 'hum': [30], 'windspeed': [10]}

    result=make_prediction(input_data = data_in)
    
    assert result["errors"]==None
    assert int(result["predictions"][0]) >=200

