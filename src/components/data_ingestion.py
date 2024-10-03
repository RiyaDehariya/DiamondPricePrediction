import os                                       #for creating path   #the output of data ingestion will have trining file, tets file,in some specific path and that path is created inside artificats file
import sys                                      #for logging and exception
from src.logger import logging                  #for calling logger.py
from src.exception import CustomException       #for callig exception.py


import pandas as pd
from sklearn.model_selection import train_test_split          #data ingestion will take data and give outup by splitting data into train and test files in some specific paths so we have to provide certain parameters to data ingestion and in this case the parameters are train path and test path
from dataclasses import dataclass                                                  


##initialize the Data Ingestion configuration
 
@dataclass                                                                                           #placeholder to create a class itself   #use of dataclass is that u can directly create class variable without using init     
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts','train.csv')                                        #providing train data paths as variables 
    test_data_path:str=os.path.join('artifacts','test.csv')                                          #providing test data paths as variables   
    raw_data_path:str=os.path.join('artifacts','raw.csv')                                            #providing raw data paths as variables 
      
##create the data ingestion class                                                                     ##for functionality

class DataIngestion:
   def __init__(self):                                                                               #whenever we create a object of data ingestion class it should have info about all 3 paths
      self.ingestion_config=DataIngestionconfig()                                                    #varibales of train,test,raw data path will be in ingestion_config class variable


   def initiate_data_ingestion(self):                                                                #whatever data ingestion that has to be happen - read data, and getting output as train, test data will happen in this folder
      logging.info('Data Ingestion method starts')                                                   #creating log that data ingestion is gong to start

      try:
         df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
         logging.info('Dataset read as pandas Dataframe')

         os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)                #creating directory  #bydefault folder location
         df.to_csv(self.ingestion_config.raw_data_path,index=False)                                               #saving datframe in raw data path


         logging.info('Raw data is created')   
         logging.info("Train test split")

         train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

         train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)            #saving train set data into this folder
         test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

         logging.info('Ingestion of data is completed')

         return(                                                                                    #retrurn two paths train and test path
            self.ingestion_config.train_data_path,
            self.ingestion_config.test_data_path

         )
                                                                                         
      
      except Exception as e:                                                                         #calling custom exception
         logging.info('Exception ocured at Data Ingestion Stage')
         raise CustomException(e,sys )                                                               #CustomException will have two parameter one is exception e and sys parameter)
      




#to test this in same folder parallely open training pipeline and run it in terminal

