from us_visa.exceptions import USvisaException
from us_visa.logger import Logging
import dill
import yaml
import os
import sys
import numpy as np

def read_yaml(file:str):
    try:
        with open(file,'rb') as f:
            yaml.safe_load(f)
    except Exception as e:
        raise USvisaException(e,sys)

def write_yaml(file_path:str,content:object,replace:bool):
    try:
        if replace=True:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file,'w') as f:
            yaml.dump(content,f)
    except Exception as e:
        raise USvisaException(e,sys)

def load_object(filepath:str)-> object:
    logging.info("Calling Load Object Function")
    try:
        if os.path.exists(filepath):
            with open(filepath,"rb") as data:
                obj=dill.load(data)

            logging.info("Succesfully loaded Object")
            return obj
        else:
            logging.info("Unable to load the object")

    except Exception as e:
        raise USvisaException(e,sys)

def save_object(filepath:str,content:object)-> None:
    logging.info("Calling Save Object Function")
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(filepath,"wb") as data:
            dill.dump(content,data)

        logging.info("Succesfully Saved Object")
        
    except Exception as e:
        raise USvisaException(e,sys)

def load_numpy_array_data(filepath:str)-> np.array:
    if os.path.exists(filepath):
        logging.info("Loading Numy Array Data")
        try:
            with open(filepath,'rb') as data:
                return np.load(data)
        except Exception as e:
            raise USvisaException(e,sys)

    else:
        logging.info("Failed Loading Numy Array Data. The filepath doesnt exist")

def save_numpy_array_data(filepath:str,content:object)-> None:
    try:
        os.makedirs(os.dirname(filepath),exist_ok=True)
        with open(filepath,'wb') as data:
            np.save(data)
        logging.info("Succesfully Saved the Numpy Array Data")
    
    except Exception as e:
        raise USvisaException(e,sys)