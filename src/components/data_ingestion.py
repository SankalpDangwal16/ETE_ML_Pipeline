import logging
import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.exception import CustomException
from src.logger import logging  # Assuming this is the correct import path

# Define DataIngestionConfig class (if not already defined above)
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact', "train.csv")
    test_data_path: str = os.path.join('artifact', "test.csv")
    raw_data_path: str = os.path.join('artifact', "data.csv")


class DataIngestion:
    def __init__(self):
        # Now it can access DataIngestionConfig because it's defined above
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Read the dataset
            logging.info("Reading dataset from CSV file...")
            df = pd.read_csv(r'C:\Users\sanka\OneDrive\Desktop\Data Science\ETE_Pipeline_Project\data\StudentsPerformance.csv')
            logging.info('Read the dataset as dataframe')

            # Save raw data
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved successfully.")

            # Split the data
            logging.info("Initiating train-test split...")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Train and Test data saved successfully.")

            # Return paths
            logging.info("Ingestion of data is done")
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            logging.error(f"Error occurred: {e}")
            raise CustomException(e, sys)

# Running the script and testing the logs
if __name__ == "__main__":
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()
