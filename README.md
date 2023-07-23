# Excel file to SQLite database with python

## General info
The Python script allows to match reported chargebacks (Excel file) with transactions from the database. Firstly I have putted an excel file to SQLite database and I made an analysis by Pandas. Then I  created an engine to connect with the database and loaded choosen data into pandas dataframes. Finally I selected and filtered data from database and matched them to data come from Excel file.
### Project includes:
- Python script - **sql_python.py**
- Analysis in Jupyter Notebook file - **Excel_to_database.ipynb**
    
### Technologies
Project is created with:
- SQL, Python 3.6,
- libraries: SQLite3, pandas.

**Running the app:**

You can run the script in the terminal:

    sql_python.py 

To run **Excel_to_database.ipynb** file use Jupyter Notebook or Google Colab.
