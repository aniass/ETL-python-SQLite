# ETL in python and SQLite

## General info
The project includes a simple ETL process using Python and SQLite database. This pipeline allows to match reported chargebacks (Excel file) with transactions from the database. 

ETL is stands for Extract, Transform and Load and it is a fundamental type of workflow in data engineering. The purpose of ETL is retrieving data from various sources,  transform it and then loading it into a data warehouse. 

#### Dataset
The dataset contains two datasets about reported chargebacks (Excel file) and transactions from the database (db.sqlite).

### Project includes:
- ETL script - **sql_python.py**
- ETL process and analysis in Jupyter Notebook file - **Excel_to_database.ipynb**

## Summary:
The project consists of classical ETL steps:

**1. Extract:**

This stage is used to extract data from data sources. 
- The data are in two formats: excel file and  SQLite database. 
- I have used pandas library to extract data from excel file into dataframe. I loaded data from the database in the same way.

**2. Transform:**
  
This stage is used for transform data. 

In this step I have used python and pandas to transform data:
- I combined the two choosen tables and filled in the missing data;
- I selected and filtered data from database and matched them to data come from Excel file.

**3. Load:**

The last stage is used to load the data that has been transformed to the database.

I have used SQLite database for storing the extracted and transformed data:
- First I have created an engine to connect with the database and loaded choosen data into pandas dataframes;
- After transform step I have created a new dataframe for transformed data;
- Finally I putted receive file to sql database.
   
### Technologies
Project is created with:
- SQL, Python 3.6,
- libraries: SQLite3, pandas.

**Running the app:**

You can run the script in the terminal:

    sql_python.py 

To run **Excel_to_database.ipynb** file use Jupyter Notebook or Google Colab.
