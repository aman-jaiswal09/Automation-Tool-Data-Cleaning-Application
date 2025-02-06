# Automation-Tool-Data-Cleaning-Application
# Data Cleaning Application

## Overview
This Python application takes datasets as input, cleans the data, and provides a cleaned version along with duplicate records. The application performs the following tasks:
- Asks for the dataset's path and name.
- Identifies and removes duplicate records while keeping a copy of them.
- Checks for missing values and handles them:
  - If a column is numeric, it replaces nulls with the mean of that column.
  - If a column is non-numeric, it drops rows containing null values.
- Saves the cleaned data and returns both the duplicate records and the cleaned dataset.

## Features
- Handles missing values intelligently.
- Keeps a record of duplicate data before removal.
- Saves cleaned data in a structured format.
- Ensures data integrity by handling numeric and categorical data separately.

## Installation
Ensure you have Python installed along with the required libraries. You can install dependencies using:
```bash
pip install pandas
pip install data_cleaning_master
```

## Usage
1. Run the script and provide the dataset's path and filename when prompted.
2. The script will process the data and handle duplicates and missing values accordingly.
3. The cleaned dataset and duplicate records will be saved as output files.
4. The script will return the cleaned dataset and duplicate records.

## Output
- **duplicates.csv**: A file containing all the removed duplicate records.
- **clean_data.csv**: The cleaned dataset after processing.

## Example
```python
data_cleaning_master.py
```
The script will then prompt for the dataset location and process it accordingly.

## Dependencies
- Python 3.x
- pandas



