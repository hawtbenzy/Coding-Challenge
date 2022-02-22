# Alternatively, reading files directly from local folder

# Importing neccessary libraries
import pandas as pd
import csv
import argparse
import glob
import os

# Creating user defined function to check datatype of csv files
def data_type():
    """
    This function checks the existing data type to enable the user know what type of data they are working with
    """
    # Storing the path to the dataset to a file list
    file_list = ["./accessories.csv", "./clothing.csv", "./household_cleaners.csv"]

    # reading the file into Python through pandas
    fixtures = pd.read_csv(io = file_list,
                            header = 0)

    fixtures.info()

# Creating user defined function to convert datatype of csv fields
def convert_data_type():
    """
    This function converts the existing data type- object into a new data type- string
    """
    # Converting data types with a dictionary
    data_types = {"email_hash" : str,
                 "category"    : str}

    # Instantiating the dataset as an object
    fixtures = pd.read_cvs(io      = file,        
                             header = 0,          
                             dtype  = data_types) # applying new data types

    # checking results
    fixtures.info()

# Creating a user defined function to merge files together
def merging_files_togther():
    """
    This function merges the three csv files into one file- stdout
    """
    # Putting file in a list 
    file_list = ["./accessories.csv", "./clothing.csv", "./household_cleaners.csv"]

    # Storing each csv file in a dataframe
    main_dataframe = pd.DataFrame(pd.read_csv(file_list[0]))

    # Using a for loop to iterate through each file
    for i in range(1,len(file_list)):
        data = pd.read_csv(file_list[i]) # reading csv files in list
        df = pd.DataFrame(data) # putting fileas together in a dataframe
        stdout = pd.concat([main_dataframe,df],axis=1) # combing the files together

    # Printing combined csv files
    print(stdout)

    # Returning output
    #return stdout

def creating_new_col():
    """
    This function creates a new column in the merged csv file and stores the file name in the new column
    """
    # Opening and reading stdout
    with open('stdout.csv', 'r') as f:
        d_reader = csv.DictReader(f)

        # print filename
        print(os.path.basename('./accessories.csv'))
        print(os.path.basename('./clothing.csv'))
        print(os.path.basename('./household_cleaners.csv'))

        # get fieldnames from DictReader object and store in list
        headers = d_reader.fieldnames

        # reading csv file
        dataFrame = pd.read_csv("./stdout.csv")
        print("DataFrame...\n",dataFrame)

        # count the rows and columns in a DataFrame
        print("\nNumber of rows and column in our DataFrame = ",dataFrame.shape)

        for line in d_reader:
            #print value in file_name for each row
            print(line['file_name'])

        # Adding new column
        dataFrame[stdout] = (dataFrame['file_name'] + line)

        print("Updated DataFrame with a new column...\n",dataFrame)

if __name__ == "__main__" :
    # holds all the information necessary to parse the command line into Python data types
    parser = argparse.ArgumentParser(description ='Takes several CSV files as arguments')
    # this store_true will store the argument as True, if present
    parser.add_argument('', type='.csv', nargs='+',
                    help='input csv files to be combined')
    args = parser.parse_args('--accepts files',nargs='*', required=False, default='')  # parsing argument

data_type(file_list=args.input)
convert_data_type(file_list=args.input)
merging_files_togther(file_list=args.input)

# For loop to print combined dataframe to console
for batch in creating_new_col(file_list=args.input):
    print(batch, end="") 
