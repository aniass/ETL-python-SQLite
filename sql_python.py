import sqlite3
import pandas as pd
from sqlite3 import Error


# Extraction
def read_excel_file(file):
    '''Rread Excel file'''
    df = pd.read_excel(file)
    df = df.rename(columns={"Transaction Datetime": "created_at",
                            "ARN": "acq_tid", "Currnecy": "currency"})
    return df

 
def read_sql(query, con):
    '''Function to read data from database'''
    df = pd.read_sql(query, con)
    return df


# Transformation
def transform_data(df1, df2):
    '''Data transformation: the matching data from excel file to data from database'''
    
    # combine the tables
    data = pd.merge(df2, df1[['Masked CCN', 'Amount', 'Card Brans', 'acq_tid']],
                how='left', on='acq_tid')
    
    # fill the missing data
    data['Amount'] = data['Amount'].fillna('0')
    data['Masked CCN'] = data['Masked CCN'].fillna('0')
    data['Amount'] = data['Amount'].astype(str)
   
    # adjust the cb value to whether there is a chargeback or not
    for index in data.index:
        if data.loc[index, 'Amount'] == '0':
            data.loc[index, 'cb'] = 0
        else:
            data.loc[index, 'cb'] = 1

    print(data['cb'].unique())

    # rename of Amount column on Amount_cb
    data = data.rename(columns={"Amount": "Amount_cb"})
    return data


# Loading
def load_data(db_name, file):
    '''Loading data: saving the transformed data in database'''
    # Create a connection with SQLite database specified by the db.sqlite file
    try:
        connection = sqlite3.connect(db_name)
        return connection
    except Error:
        print(Error)
        
    cur = connection.cursor()
    df1 = read_excel_file(file)
    df2 = read_sql('SELECT * FROM Transactions', connection)
    data = transform_data(df1, df2)
    
    # put receive file to sql database
    data.to_sql("Transactions_cb", connection, if_exists="replace")
    cur.close()
    connection.close()


if __name__ == "__main__":
    db_name = "db.sqlite"
    file = 'Processing Report.xlsx'
    load_data(db_name, file)
    
