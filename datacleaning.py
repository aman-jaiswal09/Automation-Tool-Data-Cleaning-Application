# Data cleaning App

# Importing dependencies
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random


#data_path = 'phone.csv'
#data_name = 'jan_sales'

def data_cleaning_master(data_path,data_name):

    print("Thank you for providing the details")

    sec = random.randint(1,4) #generating rando numbers
    #Print delay message
    print(f'Please wait for {sec} seconds! Checking file path')
    time.sleep(sec)

    # if the path exists
    if  not os.path.exists(data_path):
        print("Incorrect path!Try again with correct path")
        data = pd.read_csv(data_path, encoding_errors='ignore')

    else:
        # checking the file type
        if data_path.endswith('.csv'):
            print ('Dataset is csv!')
            data = pd.read_csv(data_path,encoding_errors='ignore')
        elif data_path.endswith('.xlsx'):
            print('Dataset is excel file!')
            data = pd.read_excel(data_path)
        else:
            print("Unknown file type")
            # return

    print(f' Please wait for {sec} seconds!Checking the number of columns and rows')
    time.sleep(sec)
    # showing no of records
    print(f"Dataset contain total rows : {data.shape[0]} \nTotal Columns :{data.shape[1]}")

    # start cleaning

    # duplicates
    duplicates = data.duplicated().sum()
    total_duplicates = data.duplicated().sum()

    print(f"Datasets has total duplicates records : {total_duplicates}")


    # print delay message
    print(f'Please wait for {sec} seconds! Saving total duplicates')
    time.sleep(sec)
    # saving the duplicates
    if total_duplicates > 0:
        duplicated_records = data[duplicates]
        duplicated_records.to_csv(f'{data_name}_duplicated.csv',index=None)

    # deleting duplicates
    df = data.drop_duplicates()

    # missing values
    print(f"Please wait for {sec}seconds! Checking for missing values")
    time.sleep(sec)

    # find missing values
    total_missing_values = df.isnull().sum().sum()
    missing_value_column = df.isnull().sum()

    print(f'Dataset has total missing values: {total_missing_values}')
    print(f'Dataset contain missing value by columns \n {missing_value_column}')


    # dealing with missing values
    # fillna -- int,folat
    # dropna -- object

    columns = df.columns

    for col in columns:
        if df[col].dtypes in (float,int):
            df[col] = df[col].fillna(df[col].mean())
        else:
            # dropping all rows with the missing records for non numeric col
            df[col].dropna(subset = col, inplace = True)

    print('Dataset is cleaned\n Number of Rows :{df.shape[0]}\n Number of Columns:{df.shape[1]}')

    df.to_csv(f'{data_name}_cleaned_data.csv',index = None)

    print("Dataset is saved!")

if __name__ == "__main__":

    print("Welcome  to Data Cleaning Master:")

    data_path = input("Please enter dataset path : ")
    data_name = input("Please enter dataset name : ")

    # calling function name
    data_cleaning_master(data_path,data_name)