# ETL in python and SQLite

## General info
The project includes a simple ETL process using Python and SQLite database. This pipeline allows to match reported chargebacks (Excel file) with transactions from the database. 

ETL is stands for Extract, Transform and Load and it is a fundamental type of workflow in data engineering. The purpose of ETL is retrieving data from various sources,  transform it and then loading it into a data warehouse. 

#### Dataset
The dataset contains two datasets about reported chargebacks (Excel file) and transactions from the database (db.sqlite).

### Project includes:
- ETL script - **sql_python.py**
- ETL process and analysis in Jupyter Notebook file - **Excel_to_database.ipynb**
    
### Technologies
Project is created with:
- SQL, Python 3.6,
- libraries: SQLite3, pandas.

**Running the app:**

You can run the script in the terminal:

    sql_python.py 

To run **Excel_to_database.ipynb** file use Jupyter Notebook or Google Colab.
