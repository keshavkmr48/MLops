import os
import zipfile

from abc import ABC, abstractmethod
import pandas as pd


# Define an abstract class for Data Ingestor
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path:str) -> pd.DataFrame:
        """ Abstract method to ingest data from a given file."""
        pass

# Implement a concrete class for ZIP Ingestion
class ZipIngestor(DataIngestor):

    def ingest(self,file_path:str) -> pd.DataFrame:
        """
        Extracts a .zip file and returns the content as a pandas DataFrame.
        """

        # ensure that the file is a .zip

        if not file_path.endswith(".zip"):
            raise ValueError("The provided file is not a .zip file.")
        
        # extract the zip file
        with zipfile.ZipFile(file_path,"r") as zip_ref:
            zip_ref.extractall("extracted_data")

        # find the extracted CSV file, assuming there is only one csv file.
        csv_files=[file for file in os.listdir("extrcated_data") if file.endswith(".csv")]

        if len(csv_files)==0:
            raise FileNotFoundError("No CSV file found in the extracted data.")
        if len(csv_files)>1:
            raise ValueError("Multiple CSV files found. Please specify which one to use.")
        
        # read the CSV into a dataframe
        csv_file_path = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_file_path)

        # return the dataframe
        return df
    
class DataIngestionFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) -> DataIngestor:
        """Returns the appropriate data ingestor based on the file extension."""
        if file_extension==".zip":
            return ZipIngestor()
        else:
            raise ValueError(f"No ingestor available for the file extension: {file_extension}")
        
if __name__=="__main__":
    #specify the file path

    # determine the file extension

    # get the appropriate dataingestor

    # ingest the data and load it to a dataframe
    pass

