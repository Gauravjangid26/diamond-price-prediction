import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#initiliase data ingestion configuration
@dataclass
class dataingestionconfig:
    train_data_path=os.path.join("artifacts","train.csv")
    test_data_path=os.path.join("artifacts","test.csv")
    raw_data_path=os.path.join("artifacts","raw_data.csv")
#create a data ingestion class
class data_ingestion:
    def __init__(self):
        self.ingestion_config=dataingestionconfig()

    def initiate_data_ingestion(self):
        logging.info("data ingestion method is started")

        try:
            df=pd.read_csv(os.path.join("notebook/data","Diamonds prices2022.csv"))
            logging.info("dataset read as pandas dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("train test split started ")
            train_data,test_data=train_test_split(df,test_size=0.33,random_state=30)
            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("train test split is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info("error occured in data ingestion config")