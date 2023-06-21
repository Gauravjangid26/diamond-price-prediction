import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from src.components.data_ingestion import data_ingestion
from src.components.data_transformation import datatransformation
from src.components.model_trainer import ModelTrainer

if __name__=="__main__":

    obj=data_ingestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)

    data_transformation_obj=datatransformation()
    train_arr,test_arr,pickle_data_transform_path=data_transformation_obj.initiate_data_transformation(train_data_path,test_data_path)

    model_trainer=ModelTrainer()
    model_trainer.initate_model_training(train_arr,test_arr)