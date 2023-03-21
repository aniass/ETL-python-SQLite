# Excel to sqlite database with python

## General info
This Python script allows to match reported chargebacks (excel file) with transactions from the database.  We put an excel file to SQLite database and we make an analysis by using Pandas. We create an engine to connect with our database and load chose data into pandas dataframes. We select and filter data from database and match them to data comes from excel file.

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
