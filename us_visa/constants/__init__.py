import os 
from datetime import date

Database_name="US_VISA"

COLLECTION_NAME="us_visa_data"

MONGO_DB_KEY='URL'

PIPELINE_NAME:str="usvisa"
ARTIFACT_DIR:str="artifact"

MODEL_FILE_NAME="model.pkl"

DATA_INGESTION_COLLECTION_Name:str="us_visa_data"
DATA_INGESTION_DIR_NAME:str:="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.2