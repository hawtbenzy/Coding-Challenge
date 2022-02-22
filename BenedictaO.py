# Importing neccessary libraries
import pandas as pd
import argparse
import pathlib
import csv
import os

# Creating user defined function to check datatype of csv files
def data_type():
    """
    This function checks the existing data type to enable the user know what type of data they are working with
    """
    # Storing the path to the dataset to a file list
    file_list = ["./accessories.csv", "./clothing.csv", "./household_cleaners.csv"]

    # reading the file into Python through pandas
    fixtures = pd.read_csv(io=file_list, header=0)

    fixtures.info()

# Creating user defined function to convert datatype of csv fields
def convert_data_type():
    """
    This function converts the existing data type- 'object' into a new data type- 'string'
    """
    # Converting data types with a dictionary
    data_types = {"email_hash": str, "category": str}

    # Instantiating the dataset as an object
    fixtures = pd.read_cvs(
        io=file_list, header=0, dtype=data_types
    )  # applying new data types

    # checking results
    fixtures.info()

def new_col(file_list):
    """
    This function creates a new column in the merged csv file and stores the file name in the new column
    """
    print_header = True
    # Using a for loop to go through each csv file in file list
    for file in file_list:
        # reading csv files in list using 10,000 as the max limit
        dataframe = pd.read_csv(file, chunksize=10000, iterator=True)
        filename = pathlib.Path(file).name  # getting file names
        for chunk in dataframe:
            chunk["filename"] = filename  # creating new column and storing filename
            yield chunk.to_csv(index=False, header=print_header, line_terminator = '\n') # 'index=False' - does not index file and 'line_terminator' - eliminates line space
            print_header = False

if __name__ == "__main__":
    # Using argparse library to use input from console
    parser = argparse.ArgumentParser(
        description="Combine two or more csv files together"
    )  # prompts user
    # Takes in arguments that will open command-line arguments as files
    parser.add_argument(
        nargs="+", help="csv input files location", dest="input"
    )  # input from console as list
    args = parser.parse_args()  # parsing argument

    # For loop to print combined dataframe to console
    for batch in new_col(file_list=args.input):
        print(
            batch, end=""
        )  # the end argument; prints without empty space between chunks
